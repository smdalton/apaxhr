import faker
from django.core.files.uploadedfile import SimpleUploadedFile

from core_hr.models import RegistryOfStay
from django.test import TestCase
from datetime import datetime
from core_hr.extras.core_hr_mock_factory import get_mock_user, get_mock_photo
from django.utils.timezone import  timedelta

#http://giflib.sourceforge.net/whatsinagif/bits_and_bytes.html

fake = faker.Faker()



def get_mock_ros_form(employee,expired=False, has_image=True):

    employee_address = fake.address()
    landlords_name = fake.name()
    landlords_cell_phone = fake.phone_number()
    landlords_email = fake.email()
    issued = fake.date_between(start_date="-15d", end_date="-1d")
    expiration_date = datetime.now().date() + timedelta(days=180)
    if expired:
        expiration_date = fake.date_between(start_date="-6m", end_date='-1d')
    if has_image:
        photo = get_mock_photo()
    else:
        photo = None

    form = RegistryOfStay.objects.create(
        employee=employee,
        employee_address=employee_address,
        landlords_name=landlords_name,
        landlords_cell_phone=landlords_cell_phone,
        landlords_email=landlords_email,
        issued = issued,
        expiration_date=expiration_date,
        image=photo
    )
    return form


class RosFormTestCase(TestCase):

    def setUp(self):
        self.employee = get_mock_user()
        self.ros_form = get_mock_ros_form(self.employee)

    def test_ros_form_saves_and_retrieves(self):
        retrieved_ros_form = RegistryOfStay.objects.get(id=self.ros_form.pk)
        self.assertEqual(self.ros_form, retrieved_ros_form)

    def test_ros_form_is_not_expired(self):
        valid_ros_form = get_mock_ros_form(get_mock_user(), has_image=False)
        self.assertEqual(valid_ros_form.expired, False)

    def test_ros_form_is_expired(self):
        expired_ros_form = get_mock_ros_form(get_mock_user(), expired=True)
        self.assertEqual(expired_ros_form.expired, True)

    def test_ros_form_data_complete(self):
        complete_ros_form = get_mock_ros_form(get_mock_user())
        self.assertEqual(complete_ros_form.data_complete, True)

    def test_ros_form_data_not_complete(self):
        incomplete_ros_form = get_mock_ros_form(get_mock_user(), has_image=False)
        self.assertEqual(incomplete_ros_form.data_complete, False)

#
# def test_ros_form_saves_and_retrieves(self):
#     retrieved_ros_form = ros_form.objects.get(id=self.ros_form.pk)
#     self.assertEqual(self.ros_form, retrieved_ros_form)

# def test_ros_form_expiration_function(self):
#     self.fail("add ros_form expiration function")
