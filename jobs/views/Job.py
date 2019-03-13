from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError

from user.helper.Recruiter import Recruiter
from user.helper.Token import Token
from user.helper.decorator import recruiter_login_required
from jobs.helper.constants import JOB_ADDED_SUCCESS, INVALID_JOB_STRUCTURE, JOB_UPDATED_SUCCESS, JOB_DOESNOT_EXISTS
from jobs.helper.Job import Job
import json


@recruiter_login_required
def add_job(request):
    if request.method == 'POST':

        # add job
        try:
            job_structure = json.loads(request.body.decode())

            res = Job.createUser(job_structure)

            if res == JOB_ADDED_SUCCESS:
                return HttpResponse(json.dumps({
                    'message': res
                }), content_type='application/json')

            else:
                return HttpResponseBadRequest(json.dumps({
                    'message': res
                }), content_type='application/json')

        except Exception as e:
            return HttpResponseServerError(json.dumps({
                'message': str(e)
            }), content_type='application/json')

    # Update job
    elif request.method == 'PUT':

        try:

            token = Token(request)
            user_id = token.get_user_id()
            user_type = token.get_user_type()

            recruiter = Recruiter(user_id=user_id)

            if not recruiter.has_recruiter_posted_job():
                return HttpResponseBadRequest(json.dumps({
                    'message': 'invalid access'
                }), content_type='application/json')

            job_structure = json.loads(request.body.decode())

            if "id" not in job_structure:
                return HttpResponseBadRequest(json.dumps({
                    'message': INVALID_JOB_STRUCTURE
                }), content_type='application/json')

            job_object = Job(job_structure["id"])

            res = job_object.update_job(job_structure)

            if res == JOB_UPDATED_SUCCESS:
                return HttpResponse(json.dumps({
                    'message': res
                }), content_type='application/json')

            else:
                return HttpResponseBadRequest(json.dumps({
                    'message': res
                }), content_type='application/json')

        except Exception as e:
            return HttpResponseServerError(json.dumps({
                'message': str(e)
            }), content_type='application/json')

    else:
        return HttpResponseBadRequest(json.dumps({'message': 'invalid request method'}),
                                      content_type='application/json')


def get_job(request):
    if request.method == 'GET':
        try:
            job_structure = json.loads(request.body.decode())

            if "id" not in job_structure:
                return HttpResponseBadRequest(json.dumps({
                    'message': INVALID_JOB_STRUCTURE
                }), content_type='application/json')

            job_object = Job(job_structure["id"])

            res = job_object.get_job_details()

            if res == JOB_DOESNOT_EXISTS:
                return HttpResponseBadRequest(json.dumps({
                    'message': res
                }), content_type='application/json')

            else:
                return HttpResponse(json.dumps({
                    'data': res
                }), content_type='application/json')

        except Exception as e:
            return HttpResponseServerError(json.dumps({
                'message': str(e)
            }), content_type='application/json')

    else:
        return HttpResponseBadRequest(json.dumps({'message': 'invalid request method'}),
                                      content_type='application/json')
