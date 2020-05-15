from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your tests here.

class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='ali',
            email='ali@mail.com',
            password='testpass123'
        )

        self.assertEqual(user.username,'ali')
        self.assertEqual(user.email,'ali@mail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='ali_admin',
            email='ali_admin@mail.com',
            password='testpass123'
        )

        self.assertEqual(admin_user.username,'ali_admin')
        self.assertEqual(admin_user.email,'ali_admin@mail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

class SignupPageTests(TestCase): # new
    
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
        self.response, 'Hi there! I should not be on the page.')

