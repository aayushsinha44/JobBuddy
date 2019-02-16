from django.http import HttpResponse, HttpResponseBadRequest
from user.helper.User import  User
from user.helper.Company import  Company
from user.helper.constants import COMPANY_ADDED_SUCCESS, USER_ADDED_SUCCESS
from user.helper.Token import create_token
import json


def register(request):

    if request.method == 'POST':
        user_structure = json.loads(request.body.decode())
        print (user_structure)
        res = User.createUser(user_structure)

        if res == USER_ADDED_SUCCESS:

            token = create_token(user_structure["email_id"], user_structure["type"])

            return HttpResponse(json.dumps({
                "message": "user successfully added",
                "token": token
            }), content_type='application/json')

        else:

            return HttpResponseBadRequest(json.dumps({
                "message": res
            }), content_type='application/json')

    else:
        return HttpResponseBadRequest(json.dumps({
            "message": "only post method"
        }), content_type='application/json')


def register_company(request):

    if request.method == 'POST':
        company_structure = json.loads(request.body.decode())
        res = Company.create_company(company_structure)

        if res == COMPANY_ADDED_SUCCESS:

            return HttpResponse(json.dumps({
                "message": res
            }), content_type='application/json')

        else:

            return HttpResponseBadRequest(json.dumps({
                "message": res
            }), content_type='application/json')

    else:
        return HttpResponseBadRequest(json.dumps({
            "message": "only post method"
        }), content_type='application/json')
