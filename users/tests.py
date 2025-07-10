from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class UserAuthTests(TestCase):
    def test_registration_view_loads(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Register")

    def test_login_view_loads(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Login")

    def test_user_can_register(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'TestPassword123',
            'password2': 'TestPassword123'
        })
        # Should redirect after success
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_user_login_redirects_to_dashboard(self):
        User.objects.create_user(username='testuser', password='securepass123')
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'securepass123'
        })
        self.assertRedirects(response, reverse('dashboard'))
