from user.models import CandidateModel, CandidateQualificationModel, CandidateWorkExperienceModel
from user.helper.constants import USER_EXISTS, INVALID_USER_ATTRIBUTES, USER_ADDED_SUCCESS, USER_DOESNOT_EXISTS
from user.helper.helper import process_password


class Candidate:

    def __init__(self, user_id=None):
        self.user_id = user_id
        self.user_status = self.check_user_status()

    def check_user_status(self):
        if CandidateModel.objects.filter(user_id=self.user_id).count == 0:
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
               "cv": "url"
           }
           :return: message
        """

        # Check the input structure
        if not Candidate.check_user_structure(user_structure):
            return INVALID_USER_ATTRIBUTES

        # Check whether user exists or not
        if CandidateModel.objects.filter(email_id=user_structure["email_id"],
                                         phone_number=user_structure["phone_number"]).count() > 0:
            return USER_EXISTS

        # Add user
        CandidateModel.objects.create(first_name=user_structure["first_name"],
                                      last_name=user_structure["last_name"],
                                      email_id=user_structure["email_id"],
                                      phone_number=user_structure["phone_number"],
                                      password=process_password(user_structure["password"]),
                                      location=user_structure["location"],
                                      cv=user_structure["cv"])

        return USER_ADDED_SUCCESS

    @staticmethod
    def check_user_structure(user_structure):
        candidate_user_structure = ["first_name",
                                    "last_name",
                                    "email_id",
                                    "password",
                                    "type",
                                    "location",
                                    "cv"]
        for val in candidate_user_structure:
            if val not in user_structure:
                return False
        return True

    @staticmethod
    def check_candidate(email_id=None, password=None):

        print('email')
        if CandidateModel.objects.filter(email_id=email_id,
                                         password=password).count() > 0:
            return USER_EXISTS
        return USER_DOESNOT_EXISTS

    @staticmethod
    def check_candidate(phone_number=None, password=None):

        if CandidateModel.objects.filter(phone_number=phone_number,
                                         password=password).count() > 0:
            return USER_EXISTS
        return USER_DOESNOT_EXISTS

    @staticmethod
    def get_id_from_phone_number(phone_number):

        return list(CandidateModel.objects.filter(phone_number=phone_number).values())[0]["user_id"]

    @staticmethod
    def get_id_from_email(email_id):

        return list(CandidateModel.objects.filter(email_id=email_id).values())[0]["user_id"]

    def get_details(self):

        if self.user_status == USER_DOESNOT_EXISTS:
            return USER_DOESNOT_EXISTS

        basic = list(CandidateModel.objects.filter(user_id=self.user_id).values())[0]
        basic["qualification"] = list(CandidateQualificationModel.objects.filter(
            user=CandidateModel.objects.get(user_id=self.user_id)))
        basic["work"] = list(CandidateWorkExperienceModel.objects.filter(
            user=CandidateModel.objects.get(user_id=self.user_id)))
        return basic
