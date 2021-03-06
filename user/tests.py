from django.test import TestCase, Client
from user.helper.Token import create_token, check_token, get_secret_key
from user.helper.constants import USER_ADDED_SUCCESS, VALID_TOKEN, INVALID_TOKEN, TOKEN_EXPIRED, USER_UPDATE_SUCCESS
import jwt
from user.helper.User import User
from user.models import CompanyModel, RecruiterModel


class TokenCreationAndValidationTest(TestCase):
    def setUp(self):
        self.email = "a@test1.com"
        self.type = "candidate"
        self.token = create_token(self.email, self.type)
        self.expired_token = jwt.encode({'data': self.email,
                                         'date': '2011-01-01',
                                         'type': self.type}, 'asfjoew@23r8wjfosdfn',
                                        algorithm='HS256').decode()

    def test_token(self):
        status = check_token(self.token)
        self.assertEqual(status, VALID_TOKEN)

    def test_expired_token(self):
        status = check_token(self.expired_token)
        self.assertEqual(status, TOKEN_EXPIRED)


class SecretKeyGenerationTest(TestCase):
    def setUp(self):
        self.secret_key = get_secret_key()

    def test_secret_key(self):
        self.assertEqual(self.secret_key, get_secret_key())


class CandidateCreationTest(TestCase):
    def setUp(self):
        self.user_structure_candidate = {
            "first_name": "Aayush",
            "last_name": "Sinha",
            "email_id": "aayush@gmail.com",
            "phone_number": "9876543210",
            "password": "abc1234",
            "type": "candidate",
            "location": "",
            "cv": ""
        }

    def test_candidate(self):
        res = User.createUser(self.user_structure_candidate)
        self.assertEqual(res, USER_ADDED_SUCCESS)


class RecruiterCreationTest(TestCase):
    def setUp(self):
        CompanyModel.objects.create(name="test1", sector="abc", website="abc", about="abc")
        self.user_structure = {
            "first_name": "Aayush",
            "last_name": "Sinha",
            "email_id": "aayush@gmail.com",
            "phone_number": "9876543210",
            "password": "abc1234",
            "type": "recruiter",
            "company": "1",  # Company ID
            "pan": "123"
        }

    def test_recruiter(self):
        res = User.createUser(self.user_structure)
        self.assertEqual(res, USER_ADDED_SUCCESS)


class FreelancerCreationTest(TestCase):
    def setUp(self):
        CompanyModel.objects.create(name="test1", sector="abc", website="abc", about="abc")
        self.user_structure = {
            "first_name": "Aayush",
            "last_name": "Sinha",
            "email_id": "aayush@gmail.com",
            "phone_number": "9876543210",
            "password": "abc1234",
            "type": "freelancer",
            "pan": "123",
            "location": "",
            "company": "1"
        }

    def test_recruiter(self):
        res = User.createUser(self.user_structure)
        self.assertEqual(res, USER_ADDED_SUCCESS)


class RecruiterUpdateTest(TestCase):
    def setUp(self):
        CompanyModel.objects.create(name="test1", sector="abc", website="abc", about="abc")
        self.user_structure = {
            "first_name": "Aayush",
            "last_name": "Sinha",
            "email_id": "aayush@gmail.com",
            "phone_number": "9876543210",
            "password": "abc1234",
            "type": "recruiter",
            "company": "1",  # Company ID
            "pan": "123"
        }

    def test_recruiter(self):
        res = User.createUser(self.user_structure)
        self.assertEqual(res, USER_ADDED_SUCCESS)
        user_object = User(1, self.user_structure["type"])
        self.user_structure["first_name"] = 'a'
        self.user_structure["user_id"] = 1
        del self.user_structure["password"]
        res = user_object.update_details(self.user_structure)
        self.assertEqual(res, USER_UPDATE_SUCCESS)


class FreelancerUpdateTest(TestCase):
    def setUp(self):
        CompanyModel.objects.create(name="test1", sector="abc", website="abc", about="abc")
        self.user_structure = {
            "first_name": "Aayush",
            "last_name": "Sinha",
            "email_id": "aayush@gmail.com",
            "phone_number": "9876543210",
            "password": "abc1234",
            "type": "freelancer",
            "pan": "123",
            "location": "",
            "company": "1"
        }

    def test_recruiter(self):
        res = User.createUser(self.user_structure)
        self.assertEqual(res, USER_ADDED_SUCCESS)
        user_object = User(1, self.user_structure["type"])
        self.user_structure["first_name"] = 'a'
        self.user_structure["user_id"] = 1
        del self.user_structure["password"]
        res = user_object.update_details(self.user_structure)
        self.assertEqual(res, USER_UPDATE_SUCCESS)


class CandidateUpdateTest(TestCase):
    def setUp(self):
        self.user_structure = {
            "first_name": "Aayush",
            "last_name": "Sinha",
            "email_id": "aayush@gmail.com",
            "phone_number": "9876543210",
            "password": "abc1234",
            "type": "candidate",
            "location": "",
            "cv": ""
        }

    def test_recruiter(self):
        res = User.createUser(self.user_structure)
        self.assertEqual(res, USER_ADDED_SUCCESS)
        user_object = User(1, self.user_structure["type"])
        self.user_structure["cv"] = 'abc'
        self.user_structure["user_id"] = 1
        del self.user_structure["password"]
        res = user_object.update_details(self.user_structure)
        self.assertEqual(res, USER_UPDATE_SUCCESS)

# TODO login test
# TODO create user login


