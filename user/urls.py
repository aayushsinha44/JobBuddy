from django.urls import re_path
from user.views.register import register, register_company
from user.views.login import login

urlpatterns = [
    re_path('register/', register),
    re_path('login/', login),
    re_path('register_company/', register_company),
]
