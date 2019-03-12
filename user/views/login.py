from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError
from user.helper.Token import create_token
import json
from user.helper.constants import USER_EXISTS
from user.helper.User import User


def login(request):

    if request.method == 'POST':

        try:

            res = json.loads(request.body.decode())

            data = User.check_user(res)

            if data == USER_EXISTS:

                if "phone_number" in res:
                    data = User.get_id_from_phone_number(res["phone_number"], res["type"])
                else:
                    data = User.get_id_from_email(res["email_id"], res["type"])

                token = create_token(data, res["type"])

                return HttpResponse(json.dumps({"status": "success",
                                                "token": token}), content_type='application_json')

            else:
                return HttpResponseBadRequest(json.dumps({
                    "message": data
                }), content_type='application/json')

        except Exception as e:
            return HttpResponseServerError(json.dumps({
                'message': str(e)
            }), content_type='application/json')

    else:

        return HttpResponseBadRequest(json.dumps({
            "message": "only post method"
        }), content_type='application/json')
