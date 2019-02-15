from user.models import RecruiterModel
from user.helper.constants import USER_EXISTS, INVALID_USER_ATTRIBUTES, USER_ADDED_SUCCESS


class Recruiter:

    def __init__(self, user_id=None):
        self.user_id = user_id

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
               "company": "abc",
               "pan": "4376RG4"
           }
           :return: message
        """

        # Check the input structure
        if not Recruiter.check_user_structure(user_structure):
            return INVALID_USER_ATTRIBUTES

        # Check whether user exists or not
        if RecruiterModel.objects.filter(email_id=user_structure["email"],
                                         phone_number=user_structure["phone_number"]).count() > 0:
            return USER_EXISTS

        # Add user
        RecruiterModel.objects.create(first_name=user_structure["first_name"],
                                      last_name=user_structure["last_name"],
                                      email_id=user_structure["email_id"],
                                      phone_number=user_structure["phone_number"],
                                      password=user_structure["password"],
                                      type=user_structure["type"],
                                      company=user_structure["company"],
                                      pan=user_structure["pan"])

        return USER_ADDED_SUCCESS

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
