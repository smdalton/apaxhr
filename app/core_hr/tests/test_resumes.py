from django.test import TestCase

from core_hr.extras.core_hr_mock_factory import get_mock_user

class ResumeFormTestCase(TestCase):

    def setUp(self):
        self.employee = get_mock_user()

    pass

