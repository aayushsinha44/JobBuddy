from user.models import FreelancerModel, FreelancerQualificationModel, CompanyModel
from user.helper.constants import EMAIL_EXISTS, PHONE_NUMBER, INVALID_USER_ATTRIBUTES, USER_ADDED_SUCCESS, USER_EXISTS, \
                                    USER_DOESNOT_EXISTS, COMPANY_DOESNOT_EXISTS
from user.helper.helper import process_password
from user.helper.Company import Company


class Freelancer:

    def __init__(self, user_id=None):
        self.user_id = user_id
        self.user_status = self.check_user_status()

    def check_user_status(self):
        if Freelancer.objects.filter(user_id=self.user_id).count == 0:
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
               "location": "abc",
               "pan": "4376RG4",
               "company" : "1"
           }
           :return: message
        """

        # Check the input structure
        if not Freelancer.check_user_structure(user_structure):
            return INVALID_USER_ATTRIBUTES

        # Check whether user exists or not
        if FreelancerModel.objects.filter(email_id=user_structure["email_id"]).count() > 0:
            return EMAIL_EXISTS

        if FreelancerModel.objects.filter(email_id=user_structure["phone_number"]).count() > 0:
            return PHONE_NUMBER

        company_object = Company(user_structure["company"])

        if company_object.check_company() == COMPANY_DOESNOT_EXISTS:
            return COMPANY_DOESNOT_EXISTS

        # Add user
        FreelancerModel.objects.create(first_name=user_structure["first_name"],
                                       last_name=user_structure["last_name"],
                                       email_id=user_structure["email_id"],
                                       phone_number=user_structure["phone_number"],
                                       password=process_password(user_structure["password"]),
                                       location=user_structure["location"],
                                       pan=user_structure["pan"],
                                       company=company_object.get_company_object())

        return USER_ADDED_SUCCESS

    @staticmethod
    def check_user_structure(user_structure):
        freelancer_user_structure = ["first_name",
                                     "last_name",
                                     "email_id",
                                     "password",
                                     "type",
                                     "location",
                                     "pan",
                                     "company"]
        for val in freelancer_user_structure:
            if val not in user_structure:
                return False
        return True

    @staticmethod
    def check_freelancer(email_id=None, password=None):

        if FreelancerModel.objects.filter(email_id=email_id,
                                          password=password).count() > 0:
            return USER_EXISTS
        return USER_DOESNOT_EXISTS

    @staticmethod
    def check_freelancer(phone_number=None, password=None):

        if FreelancerModel.objects.filter(phone_number=phone_number,
                                          password=password).count() > 0:
            return USER_EXISTS
        return USER_DOESNOT_EXISTS

    @staticmethod
    def get_id_from_phone_number(phone_number):

        return list(FreelancerModel.objects.filter(phone_number=phone_number).values())[0]["user_id"]

    @staticmethod
    def get_id_from_email(email_id):

        return list(FreelancerModel.objects.filter(email_id=email_id).values())[0]["user_id"]

    def get_details(self):

        if self.user_status == USER_DOESNOT_EXISTS:
            return USER_DOESNOT_EXISTS

        basic = list(Freelancer.objects.filter(user_id=self.user_id).values())[0]
        basic["qualification"] = list(FreelancerQualificationModel.objects.filter(
            user=FreelancerModel.objects.get(user_id=self.user_id)))
        del basic["password"]
        return basic

    def update_details(self, details):

        pass
