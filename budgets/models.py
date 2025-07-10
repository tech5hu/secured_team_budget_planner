from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db import models

# model to represent a budget category


class Category(models.Model):
    name = models.CharField(max_length=100)  # name category

    def __str__(self):
        return self.name  # shows the name when printed or displayed in admin

# model to represent a users budget for a specific category


class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    date = models.DateField()

    def clean(self):
        # makes sure amount is not negative
        if self.amount < 0:
            raise ValidationError("budget amount cannot be negative.")

    def __str__(self):
        # shows username and amount when printed
        return f"{self.user.username} - {self.amount}"

# model to represent a transaction


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def clean(self):
        # makes sure amount is not negative
        if self.amount < 0:
            raise ValidationError("transaction amount cannot be negative.")

    def __str__(self):
        # shows description and amount when printed
        return f"{self.description} - £{self.amount}"
