from user.helper.Recruiter import Recruiter
from user.helper.constants import INVALID_USER_TYPE, USER_EXISTS, INVALID_USER_ATTRIBUTES, USER_ADDED_SUCCESS


class User:

    def __init__(self, user_id=None):
        self._user_id = user_id

    @staticmethod
    def createUser(user_structure):
        """
        :param user_structure: {
            "first_name" : "abc",
            "last_name": "abc",
            "email_id": "a@a.com",
            "phone_number": "9876543210",
            "password": "adlbc",
            "type": "recruiter",
            ...
        }
        :return: code
        """

        # Check valid user type
        if not User.check_user(user_structure["type"]):
            return INVALID_USER_TYPE

        if user_structure["type"] == "recruiter":
            return Recruiter.create_user(user_structure)

    @staticmethod
    def check_user(user_type):
        """
        :param user_type: recruiter, freelancer, candidate
        :return: True or False
        """
        if user_type in ["recruiter", "freelancer", "candidate"]:
            return True
        return False
