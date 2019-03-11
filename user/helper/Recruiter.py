from user.helper.helper import process_password
from user.models import RecruiterModel, CompanyModel
from user.helper.constants import USER_EXISTS, INVALID_USER_ATTRIBUTES, USER_ADDED_SUCCESS, COMPANY_DOESNOT_EXISTS, \
    USER_DOESNOT_EXISTS


class Recruiter:

    def __init__(self, user_id=None):
        self.user_id = user_id
        self.user_status = self.check_user_status()

    def check_user_status(self):
        if Recruiter.objects.filter(user_id=self.user_id).count == 0:
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

        pass

    def check_details_structure(self, details):

        passe
