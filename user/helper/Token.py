from datetime import date, datetime
from user.helper.constants import TOKEN_EXPIRY_DAYS, VALID_TOKEN, INVALID_TOKEN, TOKEN_EXPIRED, INVALID_USER_TYPE, SECRET
from user.helper.User import User
import jwt
import random
import string


class Token:

    def __init__(self, request):
        self.request = request

    def get_user_id(self):
        try:
            token = self.request.META['HTTP_TOKEN']
            jwt_string = jwt.decode(token, "asfjoew@23r8wjfosdfn", algorithms=['HS256'])
            email = jwt_string["data"]
            return email
        except:
            return INVALID_TOKEN

    def get_user_type(self):
        try:
            token = self.request.META['HTTP_TOKEN']
            jwt_string = jwt.decode(token, "asfjoew@23r8wjfosdfn", algorithms=['HS256'])
            user_type = jwt_string["type"]
            return user_type
        except:
            return INVALID_TOKEN


def calculate_day_difference(token_date):
    delta = date.today() - token_date
    return int(delta.days)


def check_token(token):
    try:
        jwt_string = jwt.decode(token, 'asfjoew@23r8wjfosdfn', algorithms=['HS256'])
        # email = jwt_string["email"]
        date_login = jwt_string["date"]
        date_login = datetime.strptime(date_login, '%Y-%m-%d').date()
        diff = calculate_day_difference(date_login)
        if diff <= TOKEN_EXPIRY_DAYS:
            return VALID_TOKEN
        else:
            return TOKEN_EXPIRED
    except:
        return INVALID_TOKEN


def create_token(data, user_type):
    if not User.check_user(user_type):
        return INVALID_USER_TYPE
    token = jwt.encode({'data': data,
                        'date': str(date.today()),
                        'type': user_type}, 'asfjoew@23r8wjfosdfn', algorithm='HS256')
    token = token.decode()
    return token


SECRET_KEY = None


def get_secret_key():
    global SECRET_KEY
    if SECRET_KEY is None:
        SECRET_KEY = generate_secret_key()
        return SECRET_KEY
    else:
        return SECRET_KEY


def generate_secret_key():
    secret_key = []
    for i in range(64):
        flag = random.randint(0, 1)
        if flag == 0:
            secret_key.append(random.choice(string.digits))
        elif flag == 1:
            secret_key.append(random.choice(string.ascii_letters))
        else:
            secret_key.append(random.choice(string.punctuation))
    return "".join(secret_key)
