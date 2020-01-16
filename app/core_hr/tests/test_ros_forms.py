from django.test import TestCase
from core_hr.extras.core_hr_mock_factory import get_mock_user

class RosFormTestCase(TestCase):

    def setUp(self):
        self.employee = get_mock_user()


    #
    # def test_passport_saves_and_retrieves(self):
    #     retrieved_passport = Passport.objects.get(id=self.passport.pk)
    #     self.assertEqual(self.passport, retrieved_passport)

    # def test_passport_expiration_function(self):
    #     self.fail("add passport expiration function")
