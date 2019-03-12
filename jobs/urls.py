from django.urls import re_path
from jobs.views.Job import get_job, add_job
from user.views.login import login
from user.views.profile import profile

urlpatterns = [
    re_path('add_job/', add_job),
    re_path('get_job/', get_job)
]
