from django.http import HttpResponse, HttpResponseBadRequest
from user.helper.User import  User
from user.helper.Company import  Company
from user.helper.constants import COMPANY_ADDED_SUCCESS, USER_ADDED_SUCCESS
import json


def register(request):

    if request.method == 'POST':
        user_structure = json.loads(request.body.decode())
        res = User.createUser(user_structure)
        return HttpResponse(json.dumps({
            "message": "post method received"
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
