from django.contrib import admin
from user.models import CandidateModel, CompanyModel

# Register your models here.
admin.site.register(CandidateModel)
admin.site.register(CompanyModel)
