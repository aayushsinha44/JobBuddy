from django.urls import re_path
from user.views.register import register

urlpatterns = [
    re_path('register/', register),
]
