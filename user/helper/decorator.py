import json
from user.helper.constants import VALID_TOKEN, INVALID_TOKEN, TOKEN_EXPIRED, HTTP_UNAUTHORIZED, \
    HTTP_INTERNAL_SERVER_ERROR, RECRUITER
from user.helper.Token import check_token, Token
from django.http import HttpResponseBadRequest, HttpResponseServerError


# Login required decorator
def login_required(view):
    def inner(request):
        try:
            status = check_token(request.META['HTTP_TOKEN'])
            if status == VALID_TOKEN:
                return view(request)
            elif status == INVALID_TOKEN:
                return HttpResponseBadRequest(json.dumps({"success": False,
                                                          "code": HTTP_UNAUTHORIZED,
                                                          "message": "invalid token"}), content_type='application/json')
            elif status == TOKEN_EXPIRED:
                return HttpResponseBadRequest(json.dumps({"success": False,
                                                          "code": HTTP_UNAUTHORIZED,
                                                          "message": "token expired"}), content_type='application/json')
            else:
                return HttpResponseServerError(json.dumps({"success": False,
                                                           "code": HTTP_INTERNAL_SERVER_ERROR,
                                                           "message": "something went wrong"}),
                                               content_type='application/json')
        except:
            return HttpResponseBadRequest(json.dumps({"success": False,
                                                      "code": HTTP_UNAUTHORIZED,
                                                      "message": "login required"}), content_type='application/json')

    return inner


def recruiter_login_required(view):
    def inner(request):
        try:
            status = check_token(request.META['HTTP_TOKEN'])
            if status == VALID_TOKEN:
                token = Token(request.META['HTTP_TOKEN'])
                if token.get_user_type() == RECRUITER:
                    return view(request)
                return HttpResponseBadRequest(json.dumps({"success": False,
                                                          "code": HTTP_UNAUTHORIZED,
                                                          "message": "invalid token"}), content_type='application/json')
            elif status == INVALID_TOKEN:
                return HttpResponseBadRequest(json.dumps({"success": False,
                                                          "code": HTTP_UNAUTHORIZED,
                                                          "message": "invalid token"}), content_type='application/json')
            elif status == TOKEN_EXPIRED:
                return HttpResponseBadRequest(json.dumps({"success": False,
                                                          "code": HTTP_UNAUTHORIZED,
                                                          "message": "token expired"}), content_type='application/json')
            else:
                return HttpResponseServerError(json.dumps({"success": False,
                                                           "code": HTTP_INTERNAL_SERVER_ERROR,
                                                           "message": "something went wrong"}),
                                               content_type='application/json')
        except:
            return HttpResponseBadRequest(json.dumps({"success": False,
                                                      "code": HTTP_UNAUTHORIZED,
                                                      "message": "login required"}), content_type='application/json')

    return inner
