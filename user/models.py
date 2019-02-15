from django.db import models


# Create your models here.
class CompanyModel(models.Model):
    name = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    about = models.TextField()

    def __str__(self):
        return self.name


class UserModel(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_id = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=255)

    class Meta:
        abstract = True


class RecruiterModel(UserModel):
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)
    pan = models.CharField(max_length=100)

    def __str__(self):
        return self.user_id


class FreelancerModel(UserModel):
    pan = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user_id


class FreelancerQualificationModel(models.Model):
    user = models.ForeignKey(FreelancerModel, on_delete=models.CASCADE)
    institute_name = models.CharField(max_length=100)
    percentage = models.CharField(max_length=10)
    start_date = models.CharField(max_length=10)
    end_date = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return str(self.id)


class CandidateModel(UserModel):
    location = models.CharField(max_length=100)
    cv = models.CharField(max_length=255)  # Uploaded CV URL

    def __str__(self):
        return self.user_id


class CandidateWorkExperienceModel(models.Model):
    user = models.ForeignKey(CandidateModel, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    post = models.CharField(max_length=10)
    location = models.CharField(max_length=10)
    job_description = models.TextField()
    start_date = models.CharField(max_length=10)
    is_currently_working_here = models.BooleanField()
    end_date = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return str(self.id)


class CandidateQualificationModel(models.Model):
    user = models.ForeignKey(CandidateModel, on_delete=models.CASCADE)
    institute_name = models.CharField(max_length=100)
    percentage = models.CharField(max_length=10)
    start_date = models.CharField(max_length=10)
    end_date = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return str(self.id)
