from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        slef.admin_user = get_user_model().objects.create_superuser(
            email='michaelkarafir@gmail.com',
            password='ekhel123'
        )

        self.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='michaelkarafir@gmail.com',
            password='ekhel123',
            name='user full name'
        )

    def test_user_listed(self):
        """test jika pengguna terdaftar di halaman pengguna"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
