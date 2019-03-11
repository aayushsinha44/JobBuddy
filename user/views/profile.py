from user.helper.decorator import login_required
from django.http import HttpResponse, HttpResponseBadRequest
import json
from user.helper.User import User
from user.helper.Token import Token
from user.helper.helper import is_email, is_phone_number


@login_required
def profile(request):

    if request.method == 'GET':
        token = Token(request)
        user_id = token.get_user_id()
        user_type = token.get_user_type()

        user = User(user_id=user_id, user_type=user_type)

        response = user.get_details()
        print(user_id, user_type)

        return HttpResponse(json.dumps({
            "data": response
        }), content_type='application/json')

    elif request.method == 'PUT':

        token = Token(request)
        user_id = token.get_user_id()
        user_type = token.get_user_type()

        user = User(user_id=user_id, user_type=user_type)

        # TODO complete this

        pass

    else:
        return HttpResponseBadRequest(json.dumps({
            "message": "invalid request type"
        }), content_type='application/json')
