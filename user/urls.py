from django.urls import re_path
from user.views.register import register, register_company

urlpatterns = [
    re_path('register/', register),
    re_path('register_company/', register_company),
]
