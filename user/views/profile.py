from user.helper.decorator import login_required
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError
import json
from user.helper.User import User
from user.helper.Token import Token
from user.helper.helper import is_email, is_phone_number
from user.helper.constants import USER_UPDATE_SUCCESS


@login_required
def profile(request):
    if request.method == 'GET':

        try:
            token = Token(request)
            user_id = token.get_user_id()
            user_type = token.get_user_type()

            user = User(user_id=user_id, user_type=user_type)

            response = user.get_details()

            return HttpResponse(json.dumps({
                "data": response
            }), content_type='application/json')

        except Exception as e:
            return HttpResponseServerError(json.dumps({
                'message': str(e)
            }), content_type='application/json')

    elif request.method == 'PUT':

        try:

            token = Token(request)
            user_id = token.get_user_id()
            user_type = token.get_user_type()

            res = json.loads(request.body.decode())

            user = User(user_id=user_id, user_type=user_type)

            data = User.update_details(res)

            if data == USER_UPDATE_SUCCESS:
                return HttpResponse(json.dumps({'message': data}), content_type='application/json')

            else:
                return HttpResponseBadRequest(json.dumps({'message': data}), content_type='application/json')

        except Exception as e:
            return HttpResponseServerError(json.dumps({
                'message': str(e)
            }), content_type='application/json')

    else:
        return HttpResponseBadRequest(json.dumps({
            "message": "invalid request type"
        }), content_type='application/json')


@login_required
def candidate_work_experience(request):
    if request.method == 'GET':
        pass

    elif request.method == 'POST' or request.method == 'PUT':
        pass

    else:
        pass


@login_required
def candidate_qualification(request):
    pass


@login_required
def freelancer_qualification(request):
    pass
