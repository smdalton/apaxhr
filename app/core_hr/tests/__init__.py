from django.test import TestCase






class WorkPermitTestCase(TestCase):

    document_name = 'Work Permit'
    def setUp(self):
        self.fail('Make an employee test case')
        self.document_name = 'Work Permit'

    def test_passport_exists(self):
        self.fail(f"create and check for existence of a {self.document_name}")

    def test_passport_expired(self):
        self.fail('create several passports and an expired passport and check for expired passports')

    def test_user_exists(self):
        self.fail('Make an employee test case')


class VisaTestCase(TestCase):

    def setUp(self):
        self.fail('Make an employee test case')

    def test_passport_exists(self):
        self.fail('create and check for existence of a passport')

    def test_passport_expired(self):
        self.fail('create several passports and an expired passport and check for expired passports')

    def test_user_exists(self):
        self.fail('Make an employee test case')


class RegistryOfStayTestCase(TestCase):

    def setUp(self):
        self.fail('Make an employee test case')

    def test_passport_exists(self):
        self.fail('create and check for existence of a passport')

    def test_passport_expired(self):
        self.fail('create several passports and an expired passport and check for expired passports')

    def test_user_exists(self):
        self.fail('Make an employee test case')


class DocumentTestCase(TestCase):

    def setUp(self):
        self.fail('Make an employee test case')

    def test_passport_exists(self):
        self.fail('create and check for existence of a passport')

    def test_passport_expired(self):
        self.fail('create several passports and an expired passport and check for expired passports')

    def test_user_exists(self):
        self.fail('Make an employee test case')


class EmployeeDocumentIntegrationTestCase(TestCase):

    def setUp(self):
        self.fail(
            'Create an integration test where an employee is created,\
             and then documents are added to their model')

