from django.test import TestCase

from .models import Region, User, PowerOutageLog

class ModelTests(TestCase):

    def setUp(self):
        self.region1 = Region.objects.create(name='Jakarta Selatan', status=True)
        self.region2 = Region.objects.create(name='Jakarta Barat', status=False)
        self.user1 = User.objects.create(name='User 1', email='user1@gmail.com', region=self.region1)
        self.user2 = User.objects.create(name='User 2', email='user2@gmail.com', region=self.region2)
        self.log1 = PowerOutageLog.objects.create(region=self.region2, status=False, notified=False)
        self.log2 = PowerOutageLog.objects.create(region=self.region1, status=True, notified=True)

    def test_region_creation(self):
        self.assertEqual(self.region1.name, 'Jakarta Selatan')
        self.assertTrue(self.region1.status)

    def test_user_creation(self):
        self.assertEqual(self.user1.email, 'user1@gmail.com')
        self.assertEqual(self.user1.region, self.region1)

    def test_power_outage_log_creation(self):
        self.assertEqual(self.log1.region, self.region2)
        self.assertFalse(self.log1.status)
        self.assertFalse(self.log1.notified)
