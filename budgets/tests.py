from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.urls import reverse
from .models import Budget, Transaction, Category


class BudgetAppTests(TestCase):
    def setUp(self):
        # create a normal user and a staff user for testing permissions
        self.user = User.objects.create_user(
            username='testuser', password='securepass123')
        self.staff_user = User.objects.create_user(
            username='adminuser', password='adminpass123', is_staff=True)
        # create a category and a budget for testing
        self.category = Category.objects.create(name='General')
        self.budget = Budget.objects.create(
            user=self.user,
            category=self.category,
            amount=1000,
            description='Test budget',
            date=timezone.now().date()
        )

    def test_budget_created_correctly(self):
        # test that the budget was created with the correct values
        self.assertEqual(self.budget.user.username, 'testuser')
        self.assertEqual(self.budget.amount, 1000)
        self.assertEqual(self.budget.category.name, 'General')

    def test_transaction_negative_amount(self):
        # try to create a transaction with a negative amount and expect
        # validation to fail
        transaction = Transaction(
            user=self.user,
            description='Negative Transaction',
            amount=-50,
            date=timezone.now().date()
        )
        with self.assertRaises(ValidationError):
            transaction.full_clean()  # checks model validation rules

    def test_regular_user_cannot_access_admin_page(self):
        # login as a regular user and try to access a page only for staff
        self.client.login(username='testuser', password='securepass123')
        response = self.client.get(reverse('admin_only_page'), follow=True)

        # expect the user to be redirected to the dashboard and see a
        # permission error
        self.assertRedirects(response, reverse('dashboard'))
        self.assertContains(
            response,
            "You do not have permission to view this page.")

    def test_staff_user_can_access_admin_page(self):
        # login as a staff user and try to access the same page
        self.client.login(username='adminuser', password='adminpass123')
        response = self.client.get(reverse('admin_only_page'))

        # expect the request to succeed and contain the word "admin"
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Admin")
