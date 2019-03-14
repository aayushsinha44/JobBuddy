from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError
from user.helper.User import User
from user.helper.Company import Company
from user.helper.constants import COMPANY_ADDED_SUCCESS, USER_ADDED_SUCCESS, INVALID_ATTRIBUTES, INVALID_PAGE
from user.helper.Token import create_token, Token
import json
from user.helper.decorator import recruiter_login_required
from user.helper.Recruiter import Recruiter


def register_company(request):
    if request.method == 'POST':

        try:

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

        except Exception as e:
            return HttpResponseServerError(json.dumps({
                'message': str(e)
            }), content_type='application/json')

    else:
        return HttpResponseBadRequest(json.dumps({
            "message": "only post method"
        }), content_type='application/json')


def get_company_autocomplete(request):
    if request.method == 'GET':

        try:

            start_with = json.loads(request.body.decode())

            if "start_with" in start_with:
                return HttpResponse(json.dumps({
                    'data': Company.get_company_list(start_with["start_name"])
                }), content_type='application/json')

            else:
                return HttpResponseBadRequest(json.dumps({
                    'message': 'doesnot contains start_with'
                }), content_type='application/json')

        except Exception as e:
            return HttpResponseServerError({
                'message': str(e)
            }, content_type='application/json')

    else:
        return HttpResponseBadRequest(json.dumps({
            "message": "only get method"
        }), content_type='application/json')


def get_job_by_company(request):
    if request.method == 'GET':

        try:

            data = json.loads(request.body.decode())

            if "page_number" not in data and "company_id" not in data:
                return INVALID_ATTRIBUTES

            company = Company(data["company_id"])

            res = company.get_all_jobs_by_company(page_number=data["page_number"])
            page_size = company.get_pages_for_all_jobs()

            if res == INVALID_PAGE:
                return HttpResponseBadRequest(json.dumps({
                    'message': res
                }), content_type='application/json')

            else:
                return HttpResponse(json.dumps({
                    'pages': page_size,
                    'data': res
                }), content_type='application/json')

        except Exception as e:
            return HttpResponseServerError(json.dumps({
                'message': str(e)
            }), content_type='application/json')

    else:
        return HttpResponseBadRequest(json.dumps({
            "message": "only get method"
        }), content_type='application/json')


@recruiter_login_required
def get_job_by_recruiter(request):
    if request.method == 'GET':

        try:
            token = Token(request)
            user_id = token.get_user_id()
            user_type = token.get_user_type()

            recruiter = Recruiter(user_id=user_id)

            data = json.loads(request.body.decode())

            if "page_number" not in data:
                return INVALID_ATTRIBUTES

            res = recruiter.all_jobs_by_recruiter(page_number=data["page_number"])
            page_size = recruiter.get_page_count_for_all_jobs()

            if res == INVALID_PAGE:
                return HttpResponseBadRequest(json.dumps({
                    'message': res
                }), content_type='application/json')

            else:
                return HttpResponse(json.dumps({
                    'pages': page_size,
                    'data': res
                }), content_type='application/json')

        except Exception as e:
            return HttpResponseServerError(json.dumps({
                'message': str(e)
            }), content_type='application/json')

    else:
        return HttpResponseBadRequest(json.dumps({
            "message": "only get method"
        }), content_type='application/json')
