from jobs.helper.constants import INVALID_JOB_STRUCTURE, INVALID_JOB_TYPE, JOB_ADDED_SUCCESS
from user.helper.constants import COMPANY_DOESNOT_EXISTS
from user.helper.Company import Company
from jobs.models import JobModel


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
