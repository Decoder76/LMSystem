from django.test import TestCase
from .models import License

class LicenseModelTest(TestCase):
    def test_license_creation(self):
        license = License.objects.create(key="ABC123", is_active=True)
        self.assertEqual(license.key, "ABC123")
