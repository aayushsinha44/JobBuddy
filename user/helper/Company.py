import math
from user.models import CompanyModel
from user.helper.constants import COMPANY_EXISTS, COMPANY_ADDED_SUCCESS, INVALID_COMPANY_ATTRIBUTES, \
    COMPANY_DOESNOT_EXISTS, JOB_PAGE_SIZE, INVALID_PAGE
from jobs.models import JobModel


class Company:

    # TODO Complete this
    SECTOR = ['IT', 'Finance', 'Marketing']

    def __init__(self, company_id=None):
        self.company_id = company_id

    @staticmethod
    def create_company(company_structure):
        """
           :param company_structure: {
               "name" : "abc",
               "sector": "IT",
               "website": "https://company.com",
               "about": "text",
           }
           :return: message
        """

        # Check the input structure
        if not Company.check_company_structure(company_structure):
            return INVALID_COMPANY_ATTRIBUTES

        # Check whether company exists or not
        if CompanyModel.objects.filter(name=company_structure["name"]).count() > 0:
            return COMPANY_EXISTS

        if company_structure["sector"] not in Company.SECTOR:
            return INVALID_COMPANY_ATTRIBUTES

        CompanyModel.objects.create(name=company_structure["name"],
                                    sector=company_structure["sector"],
                                    website=company_structure["website"],
                                    about=company_structure["about"])

        return COMPANY_ADDED_SUCCESS

    @staticmethod
    def check_company_structure(company_structure):
        company_structure_list = ["name",
                                  "sector",
                                  "website",
                                  "about"]
        for val in company_structure_list:
            if val not in company_structure:
                return False
        return True

    def check_company(self):

        if CompanyModel.objects.filter(id=self.company_id).count() == 0:
            return COMPANY_DOESNOT_EXISTS

        return COMPANY_EXISTS

    def get_company_object(self):
        return CompanyModel.objects.get(id=self.company_id)

    @staticmethod
    def get_company_list(self, start_name):
        return list(CompanyModel.objects.filter(name__contains=start_name).values())

    def get_all_jobs_by_company(self, page_number):

        company_object = self.get_company_object()

        pages = self.get_pages_for_all_jobs()

        if page_number > pages:
            return INVALID_PAGE

        low = (page_number-1)*JOB_PAGE_SIZE
        high = page_number*JOB_PAGE_SIZE

        if pages == page_number:
            return JobModel.objects.filter(company=company_object).values()[low:]

        return JobModel.objects.filter(company=company_object).values()[low:high]

    def get_pages_for_all_jobs(self):
        company_object = self.get_company_object()

        job_count = JobModel.objects.filter(company=company_object).count()
        pages = math.ceil(job_count / JOB_PAGE_SIZE)

        return pages
