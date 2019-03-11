from user.models import CompanyModel
from user.helper.constants import COMPANY_EXISTS, COMPANY_ADDED_SUCCESS, INVALID_COMPANY_ATTRIBUTES, COMPANY_DOESNOT_EXISTS


class Company:

    # TODO Complete this
    SECTOR = (
        ('IT', 'Information Technology'),
        ('TRAVEL', 'Travel and Tourism'),
        ('FN', 'Finance')
    )

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

        # Add user
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
    def get_company_list():
        pass

