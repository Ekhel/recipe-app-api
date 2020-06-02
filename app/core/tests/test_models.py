from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_email_succesfull(self):
        """Test Buat User Baru dengan email Custom"""
        email = 'michaelkarafir@gmail.com'
        password = 'ekhel123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    
    def test_new_user_email_normalize(self):
        """Test Buat User dengan Email yang sudah di normalisasi"""
        email = "michaelkarafir@GMAIL.COM"
        user = get_user_model().objects.create_user(email, 'ekhel123')

        self.assertEqual(user.email, email.lower())

    
    def test_user_invalid_email(self):
        """Test Buat User dengan Validasi Email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'ekhel123')


    def test_create_new_superuser(self):
        "test buat superuser baru"
        user = get_user_model().objects.create_superuser(
            'michaelkarafir@gmail.com',
            'ekhel123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_start)