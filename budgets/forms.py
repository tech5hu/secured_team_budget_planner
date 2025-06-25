from django import forms  
from .models import Budget, Transaction  
from django.core.exceptions import ValidationError  

# form to handle budget creation and editing
class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget  # form based on the budget model
        fields = ['category', 'amount', 'description', 'date']  # these fields will appear in the form
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})  # makes the date field use a calendar picker
        }

    # custom validation to make sure amount is more than 0
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise ValidationError("amount must be greater than zero.")
        return amount

    # custom validation to make sure description is not too short
    def clean_description(self):
        desc = self.cleaned_data.get('description')
        if len(desc.strip()) < 3:
            raise ValidationError("description must be at least 3 characters long.")
        return desc


# form to handle transaction creation and editing
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction  # form based on the transaction model
        fields = ['description', 'amount']  # only two fields in this form

    # custom validation to make sure transaction amount is more than 0
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise ValidationError("transaction amount must be greater than £0.")
        return amount

    # custom validation to make sure description is not too short
    def clean_description(self):
        desc = self.cleaned_data.get('description')
        if len(desc.strip()) < 3:
            raise ValidationError("description must be at least 3 characters long.")
        return desc
