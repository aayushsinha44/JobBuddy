from user.helper.helper import process_password
from user.models import RecruiterModel, CompanyModel
from user.helper.constants import USER_EXISTS, INVALID_USER_ATTRIBUTES, USER_ADDED_SUCCESS, COMPANY_DOESNOT_EXISTS, \
    USER_DOESNOT_EXISTS, USER_UPDATE_SUCCESS, INVALID_PAGE, JOB_PAGE_SIZE
from user.helper.Company import Company
from jobs.models import JobModel


class Recruiter:

    def __init__(self, user_id=None):
        self.user_id = user_id
        self.user_status = self.check_user_status()

    def check_user_status(self):
        if RecruiterModel.objects.filter(user_id=self.user_id).count() == 0:
            return USER_DOESNOT_EXISTS
        return USER_EXISTS

    @staticmethod
    def create_user(user_structure):
        """
           :param user_structure: {
               "first_name" : "abc",
               "last_name": "abc",
               "email_id": "a@a.com",
               "phone_number": "9876543210",
               "password": "adlbc",
               "type": "recruiter",
               "company": "214", # Company id
               "pan": "4376RG4"
           }
           :return: message
        """

        # Check the input structure
        if not Recruiter.check_user_structure(user_structure):
            return INVALID_USER_ATTRIBUTES

        # Check whether user exists or not
        if RecruiterModel.objects.filter(email_id=user_structure["email_id"],
                                         phone_number=user_structure["phone_number"]).count() > 0:
            return USER_EXISTS

        # Check whether company exists or not
        if not Recruiter.check_company(user_structure["company"]):
            return COMPANY_DOESNOT_EXISTS

        # Add user
        RecruiterModel.objects.create(first_name=user_structure["first_name"],
                                      last_name=user_structure["last_name"],
                                      email_id=user_structure["email_id"],
                                      phone_number=user_structure["phone_number"],
                                      password=process_password(user_structure["password"]),
                                      company=CompanyModel.objects.get(id=user_structure["company"]),
                                      pan=user_structure["pan"])

        return USER_ADDED_SUCCESS

    @staticmethod
    def check_company(company_id):

        if CompanyModel.objects.filter(id=company_id).count() == 0:
            return False
        return True

    @staticmethod
    def check_user_structure(user_structure):
        recruiter_user_structure = ["first_name",
                                    "last_name",
                                    "email_id",
                                    "password",
                                    "type",
                                    "company",
                                    "pan"]
        for val in recruiter_user_structure:
            if val not in user_structure:
                return False
        return True

    @staticmethod
    def check_recruiter(email_id=None, password=None):

        if RecruiterModel.objects.filter(email_id=email_id,
                                         password=password).count() > 0:
            return USER_EXISTS
        return USER_DOESNOT_EXISTS

    @staticmethod
    def check_recruiter(phone_number=None, password=None):

        if RecruiterModel.objects.filter(phone_number=phone_number,
                                         password=password).count() > 0:
            return USER_EXISTS
        return USER_DOESNOT_EXISTS

    @staticmethod
    def get_id_from_phone_number(phone_number):

        return list(RecruiterModel.objects.filter(phone_number=phone_number).values())[0]["user_id"]

    @staticmethod
    def get_id_from_email(email_id):

        return list(RecruiterModel.objects.filter(email_id=email_id).values())[0]["user_id"]

    def get_details(self):

        if self.user_status == USER_DOESNOT_EXISTS:
            return USER_DOESNOT_EXISTS

        basic = list(RecruiterModel.objects.filter(user_id=self.user_id).values())[0]
        basic["company"] = list(CompanyModel.objects.filter(id=basic["company"]))[0]
        del basic["password"]
        return basic

    def update_details(self, details):

        if self.check_details_structure(details):

            if self.check_recruiter():

                company_object = Company(details["company"])

                if not company_object.check_company():
                    return COMPANY_DOESNOT_EXISTS

                recruiter_object = self.get_recruiter_object()
                recruiter_object.first_name = details["first_name"]
                recruiter_object.last_name = details["last_name"]
                recruiter_object.company = company_object.get_company_object()
                recruiter_object.pan = details["pan"]
                recruiter_object.save()

                return USER_UPDATE_SUCCESS

            else:
                return USER_DOESNOT_EXISTS

        else:
            return INVALID_USER_ATTRIBUTES

    def check_details_structure(self, details):
        recruiter_user_structure = ["first_name",
                                    "last_name",
                                    "email_id",
                                    "user_id",
                                    "type",
                                    "company",
                                    "pan"]
        for val in recruiter_user_structure:
            if val not in details:
                return False
        return True

    def check_recruiter(self):
        # Check whether user exists or not
        if RecruiterModel.objects.filter(user_id=self.user_id).count() > 0:
            return True
        return False

    def get_recruiter_object(self):
        return RecruiterModel.objects.get(user_id=self.user_id)

    def all_jobs_by_recruiter(self, page_number):

        pages = self.get_page_count_for_all_jobs()
        recruiter_object = self.get_recruiter_object()

        if page_number > pages:
            return INVALID_PAGE

        low = (page_number-1)*JOB_PAGE_SIZE
        high = page_number*JOB_PAGE_SIZE

        if pages == page_number:
            return JobModel.objects.filter(recruiter=recruiter_object).values()[low:]

        return JobModel.objects.filter(recruiter=recruiter_object).values()[low:high]

    def get_page_count_for_all_jobs(self):
        recruiter_object = self.get_recruiter_object()

        pages = JobModel.objects.filter(recruiter=recruiter_object).count()

        return pages

    def has_recruiter_posted_job(self, job_id):
        recruiter_object = self.get_recruiter_object()

        if JobModel.objects.filter(recruiter=recruiter_object).count > 0:
            return True
        return False
