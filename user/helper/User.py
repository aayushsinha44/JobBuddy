from user.helper.Recruiter import Recruiter
from user.helper.Candidate import Candidate
from user.helper.Freelancer import Freelancer
from user.helper.constants import INVALID_USER_TYPE, INVALID_ATTRIBUTES, RECRUITER, FREELANCER, CANDIDATE, \
    INVALID_PHONE_NUMBER
from user.helper.helper import process_password


class User:

    def __init__(self, user_id, user_type):
        self._user_id = user_id
        self.user_type = user_type

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
        if not User.check_user_structure(user_structure["type"]):
            return INVALID_USER_TYPE

        # Check phone number
        if not User.check_phone_number(user_structure["phone_number"]):
            return INVALID_PHONE_NUMBER

        # Create user
        if user_structure["type"] == RECRUITER:
            return Recruiter.create_user(user_structure)
        elif user_structure["type"] == FREELANCER:
            return Freelancer.create_user(user_structure)
        elif user_structure["type"] == CANDIDATE:
            return Candidate.create_user(user_structure)

    @staticmethod
    def check_phone_number(phone_number):

        try:
            phone_number = int(phone_number)
            if len(str(phone_number)) == 10:
                return True
            return False
        except:
            return False

    @staticmethod
    def check_user_structure(user_type):
        """
        :param user_type: recruiter, freelancer, candidate
        :return: True or False
        """
        if user_type in [RECRUITER, FREELANCER, CANDIDATE]:
            return True
        return False

    @staticmethod
    def check_user(login_structure):
        """Check user exists or not"""

        if "password" not in login_structure and \
                "type" not in login_structure \
                and ("email_id" not in login_structure or "phone_number" not in login_structure):
            return INVALID_ATTRIBUTES

        if not User.check_user(login_structure["type"]):
            return INVALID_USER_TYPE

        if "email_id" in login_structure:

            email_id = login_structure["email_id"]
            password = process_password(login_structure["password"])

            if login_structure["type"] == RECRUITER:
                return Recruiter.check_recruiter_email(email_id=email_id,
                                                 password=password)

            elif login_structure["type"] == FREELANCER:
                return Freelancer.check_freelancer(email_id=email_id,
                                                   password=password)

            elif login_structure["type"] == CANDIDATE:
                return Candidate.check_candidate_email(email_id=email_id,
                                                 password=password)

        elif "phone_number" in login_structure:

            phone_number = login_structure["phone_number"]
            password = process_password(login_structure["password"])

            if login_structure["type"] == RECRUITER:
                return Recruiter.check_recruiter_phone(phone_number=phone_number,
                                                 password=password)

            elif login_structure["type"] == FREELANCER:
                return Freelancer.check_freelancer(phone_number=phone_number,
                                                   password=password)

            elif login_structure["type"] == CANDIDATE:
                return Candidate.check_candidate_phone(phone_number=phone_number,
                                                 password=password)

    @staticmethod
    def get_id_from_phone_number(phone_number, user_type):
        if not User.check_user_structure(user_type):
            return INVALID_USER_TYPE

        if user_type == RECRUITER:
            return Recruiter.get_id_from_phone_number(phone_number)

        elif user_type == FREELANCER:
            return Freelancer.get_id_from_phone_number(phone_number)

        elif user_type == CANDIDATE:
            return Candidate.get_id_from_phone_number(phone_number)

    @staticmethod
    def get_id_from_email(email_id, user_type):
        if not User.check_user_structure(user_type):
            return INVALID_USER_TYPE

        if user_type == RECRUITER:
            return Recruiter.get_id_from_email(email_id)

        elif user_type == FREELANCER:
            return Freelancer.get_id_from_email(email_id)

        elif user_type == CANDIDATE:
            return Candidate.get_id_from_email(email_id)

    def get_details(self):

        if not User.check_user_structure(self.user_type):
            return INVALID_USER_TYPE

        if self.user_type == RECRUITER:
            recruiter = Recruiter(self._user_id)
            return recruiter.get_details()

        elif self.user_type == FREELANCER:
            freelancer = Freelancer(self._user_id)
            return freelancer.get_details()

        elif self.user_type == CANDIDATE:
            candidate = Candidate(self._user_id)
            return candidate.get_details()

    def update_details(self, details):

        if not User.check_user_type(self.user_type):
            return INVALID_USER_TYPE

        if self.user_type == RECRUITER:
            recruiter = Recruiter(self._user_id)
            return recruiter.update_details(details)

        elif self.user_type == FREELANCER:
            freelancer = Freelancer(self._user_id)
            return freelancer.update_details(details)

        elif self.user_type == CANDIDATE:
            candidate = Candidate(self._user_id)
            return candidate.update_details(details)

    @staticmethod
    def check_user_type(user_type):
        if user_type in [RECRUITER, CANDIDATE, FREELANCER]:
            return True
        return False
