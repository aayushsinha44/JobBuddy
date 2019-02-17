from user.helper.decorator import login_required
from django.http import HttpResponse, HttpResponseBadRequest
import json
from user.helper.User import User
from user.helper.Token import Token
from user.helper.helper import is_email, is_phone_number


@login_required
def get_details(request):

    token = Token(request)
    data = Token.get_email()

    user = User()
