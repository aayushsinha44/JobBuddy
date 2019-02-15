from user.helper.Recruiter import Recruiter
from user.helper.Candidate import Candidate
from user.helper.Freelancer import Freelancer
from user.helper.constants import INVALID_USER_TYPE


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

        # Create user
        if user_structure["type"] == "recruiter":
            return Recruiter.create_user(user_structure)
        elif user_structure["type"] == "freelancer":
            return Freelancer.create_user(user_structure)
        elif user_structure["type"] == "candidate":
            return Candidate.create_user(user_structure)

    @staticmethod
    def check_user(user_type):
        """
        :param user_type: recruiter, freelancer, candidate
        :return: True or False
        """
        if user_type in ["recruiter", "freelancer", "candidate"]:
            return True
        return False
