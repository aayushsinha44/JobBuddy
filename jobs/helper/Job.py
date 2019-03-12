from jobs.helper.constants import INVALID_JOB_STRUCTURE, INVALID_JOB_TYPE, JOB_ADDED_SUCCESS, JOB_UPDATED_SUCCESS, \
    JOB_DOESNOT_EXISTS
from jobs.models import JobModel
from user.helper.Company import Company
from user.models import CompanyModel
from user.helper.constants import COMPANY_DOESNOT_EXISTS


class Job:

    def __init__(self, job_id):
        self.job_id = job_id

    @staticmethod
    def add_job(job_structure):

        if Job.check_job_structure(job_structure):

            if not Job.check_job_type(job_structure["job_type"]):
                return INVALID_JOB_TYPE

            company_object = Company(job_structure["company"])

            if company_object.check_company() == COMPANY_DOESNOT_EXISTS:
                return COMPANY_DOESNOT_EXISTS

            JobModel.objects.create(company= company_object.get_company_object(),
                                    job_title=job_structure["job_title"],
                                    job_type=job_structure["job_type"],
                                    job_qualification=job_structure["job_qualification"],
                                    job_location=job_structure["job_location"],
                                    salary_range_min=job_structure["salary_range_min"],
                                    salary_range_max=job_structure["salary_range_max"],
                                    work_experience_min=job_structure["work_experience_min"],
                                    work_experience_max=job_structure["work_experience_max"],
                                    no_of_opening=job_structure["no_of_opening"],
                                    job_description=job_structure["job_description"])

            return JOB_ADDED_SUCCESS

        else:
            return INVALID_JOB_STRUCTURE

    def update_job(self, job_structure):

        if Job.check_job_structure(job_structure):

            if not Job.check_job_type(job_structure["job_type"]):
                return INVALID_JOB_TYPE

            job_object = self.get_job_object()

            company_object = Company(job_structure["company"])

            if company_object.check_company() == COMPANY_DOESNOT_EXISTS:
                return COMPANY_DOESNOT_EXISTS

            job_object.company = company_object.get_company_object()
            job_object.title = job_structure["job_title"]
            job_object.job_type = job_structure["job_type"]
            job_object.job_qualification = job_structure["job_qualification"]
            job_object.job_location = job_structure["job_location"]
            job_object.salary_range_min = job_structure["salary_range_min"]
            job_object.salary_range_max = job_structure["salary_range_max"]
            job_object.work_experience_min = job_structure["work_experience_min"]
            job_object.work_experience_max = job_structure["work_experience_max"]
            job_object.no_of_opening = job_structure["no_of_opening"]
            job_object.job_description = job_structure["job_description"]

            job_object.save()

            return JOB_UPDATED_SUCCESS

        else:
            return INVALID_JOB_STRUCTURE

    @staticmethod
    def check_job_structure(job_structure):
        data_key = ["company", "job_title", "job_type", "job_qualification", "job_location", "salary_range_min",
                    "salary_range_max", "work_experience_min", "work_experience_max", "no_of_opening",
                    "job_description"]

        for key in data_key:
            if key not in job_structure:
                return False
        return True

    @staticmethod
    def check_job_type(job_type):
        for job_option in JobModel.JOB_OPTIONS:
            if job_option[0] == job_type:
                return True
        return False

    def get_job_object(self):
        return JobModel.objects.get(id=self.job_id)

    def check_job(self):
        if JobModel.objects.filter(id=self.job_id).count() > 0:
            return True
        return False

    def get_job_details(self):
        if not self.check_job():
            return JOB_DOESNOT_EXISTS
        basic = list(JobModel.objects.filter(id=self.job_id).values())[0]
        basic["company"] = str(basic["company_id"])
        del basic["company_id"]
        return basic
