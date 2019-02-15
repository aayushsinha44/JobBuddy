from django.test import TestCase
from user.helper.Token import create_token, check_token, get_secret_key
from user.helper.constants import TOKEN_EXPIRY_DAYS, VALID_TOKEN, INVALID_TOKEN, TOKEN_EXPIRED
import jwt


class TokenCreationAndValidationTest(TestCase):
    def setUp(self):
        self.email = "a@test1.com"
        self.type = "candidate"
        self.token = create_token(self.email, self.type)
        self.expired_token = jwt.encode({'email': self.email,
                                         'date': '2011-01-01',
                                         'type': self.type}, get_secret_key(),
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
