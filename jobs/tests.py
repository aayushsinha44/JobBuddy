from django.test import TestCase
from jobs.helper.constants import JOB_ADDED_SUCCESS, INVALID_JOB_TYPE, INVALID_JOB_STRUCTURE, JOB_UPDATED_SUCCESS
from user.models import CompanyModel
from jobs.helper.Job import Job
from user.helper.User import User


# Create your tests here.
class JobCreationTest(TestCase):
    def setUp(self):
        CompanyModel.objects.create(name="test1", sector="abc", website="abc", about="abc")
        self.job_structure = {
            "recruiter": 1,
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
        self.user_structure = {
            "first_name": "Aayush",
            "last_name": "Sinha",
            "email_id": "aayush@gmail.com",
            "phone_number": "9876543210",
            "password": "abc1234",
            "type": "recruiter",
            "company": "1",  # Company ID
            "pan": "123"
        }
        User.createUser(self.user_structure)
        self.job_structure_invalid = {
            "recruiter": 1,
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
            "recruiter": 1,
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


class JobUpdationTest(TestCase):
    def setUp(self):
        CompanyModel.objects.create(name="test1", sector="abc", website="abc", about="abc")
        self.job_structure = {
            "recruiter": 1,
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
        self.user_structure = {
            "first_name": "Aayush",
            "last_name": "Sinha",
            "email_id": "aayush@gmail.com",
            "phone_number": "9876543210",
            "password": "abc1234",
            "type": "recruiter",
            "company": "1",  # Company ID
            "pan": "123"
        }
        User.createUser(self.user_structure)
        Job.add_job(self.job_structure)

    def test_job(self):
        self.job_structure["id"]=1
        job_object = Job(self.job_structure["id"])
        res = job_object.update_job(self.job_structure)
        self.assertEqual(res, JOB_UPDATED_SUCCESS)


class JobGetTest(TestCase):
    def setUp(self):
        CompanyModel.objects.create(name="test1", sector="abc", website="abc", about="abc")
        self.job_structure = {
            "recruiter": 1,
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
        self.user_structure = {
            "first_name": "Aayush",
            "last_name": "Sinha",
            "email_id": "aayush@gmail.com",
            "phone_number": "9876543210",
            "password": "abc1234",
            "type": "recruiter",
            "company": "1",  # Company ID
            "pan": "123"
        }
        User.createUser(self.user_structure)
        Job.add_job(self.job_structure)
        self.job_structure["id"] = 1

    def test_job(self):
        job_object = Job(self.job_structure["id"])
        res = job_object.get_job_details()
        self.assertEqual(res, self.job_structure)
