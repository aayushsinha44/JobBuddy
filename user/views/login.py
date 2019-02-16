from django.http import HttpResponse, HttpResponseBadRequest
from user.helper.Token import create_token
import json


def login(request):

    if request.method == 'POST':

        res = json.loads(request.body.decode())


    else:

        return HttpResponseBadRequest(json.dumps({
            "message": "only post method"
        }), content_type='application/json')
