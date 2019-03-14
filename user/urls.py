from django.urls import re_path
from user.views.register import register
from user.views.Company import register_company, get_company_autocomplete, get_job_by_company, get_job_by_recruiter
from user.views.login import login
from user.views.profile import profile

urlpatterns = [
    re_path('register/', register),
    re_path('login/', login),
    re_path('register_company/', register_company),
    re_path('get_company_autocomplete/', get_company_autocomplete),
    re_path('profile/', profile),
    re_path('job_by_company/', get_job_by_company),
    re_path('job_by_recruiter/', get_job_by_recruiter),
]
