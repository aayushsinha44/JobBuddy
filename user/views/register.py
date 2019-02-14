from django.http import HttpResponse, HttpResponseBadRequest
from user.helper.User import  User
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
