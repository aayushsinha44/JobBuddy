from django.test import TestCase
from jobs.helper.constants import JOB_ADDED_SUCCESS, INVALID_JOB_TYPE, INVALID_JOB_STRUCTURE
from user.models import CompanyModel
from jobs.helper.Job import Job


# Create your tests here.
class RecruiterCreationTest(TestCase):
    def setUp(self):
        CompanyModel.objects.create(name="test1", sector="abc", website="abc", about="abc")
        self.job_structure = {
            "company": "1",
            "job_title": "SR Manager",
            "job_type": "FT",
            "job_qualification": "MBA Passout",
            "job_location": "Mumbai",
            "salary_range_min": None,
            "salary_range_max": None,
            "work_experience_min": None,
            "work_experience_max": None,
            "no_of_opening": None,
            "job_description": "Manager"
        }
        self.job_structure_invalid = {
            "company": "1",
            "job_title": "SR Manager",
            "job_type": "FT",
            "job_qualification": "MBA Passout",
            "job_location": "Mumbai",
            "salary_range_min": None,
            "salary_range_max": None,
            "work_experience_min": None,
            "work_experience_max": None,
            "job_description": "Manager"
        }
        self.job_structure_invalid_type = {
            "company": "1",
            "job_title": "SR Manager",
            "job_type": "FT1",
            "job_qualification": "MBA Passout",
            "job_location": "Mumbai",
            "salary_range_min": None,
            "salary_range_max": None,
            "work_experience_min": None,
            "work_experience_max": None,
            "no_of_opening": None,
            "job_description": "Manager"
        }

    def test_job(self):
        res = Job.add_job(self.job_structure)
        self.assertEqual(res, JOB_ADDED_SUCCESS)
        res = Job.add_job(self.job_structure_invalid)
        self.assertEqual(res, INVALID_JOB_STRUCTURE)
        res = Job.add_job(self.job_structure_invalid_type)
        self.assertEqual(res, INVALID_JOB_TYPE)


