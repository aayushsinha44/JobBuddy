from django.db import models
from user.models import FreelancerModel, CompanyModel, CandidateModel


# Create your models here.
class JobModel(models.Model):

    JOB_OPTIONS = (
        ('FT', 'Full Time'),
        ('IN', 'Intern'),
        ('PT', 'Part Time'),
        ('CN', 'Contract')
    )

    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100, choices=JOB_OPTIONS)
    job_qualification = models.TextField()
    job_location = models.CharField(max_length=255)
    salary_range_min = models.BigIntegerField(blank=True, null=True)
    salary_range_max = models.BigIntegerField(blank=True, null=True)
    work_experience_min = models.BigIntegerField(blank=True, null=True)
    work_experience_max = models.BigIntegerField(blank=True, null=True)
    no_of_opening = models.BigIntegerField(blank=True, null=True)
    job_description = models.TextField()

    def __str__(self):
        return str(self.id)


class CandidateJobStatusModel(models.Model):

    CURRENT_STATUS = (
        ('1', 'No freelancer tagged'),
        ('2', 'freelancer authorisation pending'),
        ('3', '')
    )

    status = models.CharField(max_length=100, choices=CURRENT_STATUS)
    candidate = models.ForeignKey(CandidateModel, on_delete=models.CASCADE)


class FreelancerJobTakeAwayModel(models.Model):
    freelancer = models.ForeignKey(FreelancerModel, on_delete=models.CASCADE)
    job = models.ForeignKey(JobModel, on_delete=models.CASCADE)


class JobQuestionModel(models.Model):
    job = models.ForeignKey(JobModel, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)


class JobAnswerModel(models.Model):
    job_question = models.ForeignKey(JobQuestionModel, on_delete=models.CASCADE)
    candidate_id = models.ForeignKey(CandidateModel, on_delete=models.CASCADE)
    answer = models.TextField()

    def __str__(self):
        return str(self.id)

