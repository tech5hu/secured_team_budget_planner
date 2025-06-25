from django.shortcuts import render, redirect, get_object_or_404
from .models import Budget, Transaction
from .forms import BudgetForm, TransactionForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from .decorators import staff_required

# home page view
def home(request):
    return render(request, 'users/home.html')

# shows the current users personal budgets
@login_required
def my_budgets(request):
    budgets = Budget.objects.filter(user=request.user)
    return render(request, 'budgets/my_budgets.html', {'budgets': budgets})

# lets users add a new budget
@login_required
def add_budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)  # don't save to db yet
            budget.user = request.user  # attach the logged in user
            try:
                budget.full_clean()  # run custom model validation
                budget.save()  # now save to database
                messages.success(request, 'budget added successfully!')
                return redirect('my_budgets')
            except ValidationError as e:
                form.add_error(None, e.message_dict)
        else:
            messages.error(request, 'please correct the errors below.')
    else:
        form = BudgetForm()
    return render(request, 'budgets/add_budgets.html', {'form': form})

# lets users delete their budget with confirmation
@login_required
def delete_budget(request, pk):
    budget = get_object_or_404(Budget, pk=pk)
    if request.method == 'POST':
        budget.delete()
        return redirect('my_budgets')
    return render(request, 'budgets/confirm_delete_budget.html', {'object': budget})

# shows the list of the users own transactions
@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    return render(request, 'budgets/transaction_list.html', {'transactions': transactions})

# lets users add a new transaction
@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            try:
                transaction.full_clean()  # check validation
                transaction.save()
                messages.success(request, 'transaction added!')
                return redirect('transaction_list')
            except ValidationError as e:
                form.add_error(None, e.message_dict)
        else:
            messages.error(request, 'please fix the form errors.')
    else:
        form = TransactionForm()
    return render(request, 'budgets/add_transaction.html', {'form': form})

# lets users delete a transaction if they own it or are an admin
@login_required
def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if not request.user.is_superuser and transaction.user != request.user:
        messages.error(request, "you do not have permission to delete this transaction.")
        return redirect('transaction_list')

    if request.method == 'POST':
        transaction.delete()
        messages.success(request, "transaction deleted successfully.")
        return redirect('transaction_list')
    return render(request, 'budgets/confirm_delete_transaction.html', {'transaction': transaction})

# lets users edit their own budget (or admins can edit any)
@login_required
def edit_budget(request, pk):
    budget = get_object_or_404(Budget, pk=pk)
    if not request.user.is_superuser and budget.user != request.user:
        messages.error(request, "you do not have permission to edit this budget.")
        return redirect('my_budgets')

    form = BudgetForm(request.POST or None, instance=budget)
    if form.is_valid():
        form.save()
        messages.success(request, "budget updated successfully.")
        return redirect('my_budgets')

    return render(request, 'budgets/edit_budget.html', {'form': form})

# lets users edit a transaction if its theirs or if they are admin
@login_required
def edit_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if not request.user.is_superuser and transaction.user != request.user:
        messages.error(request, "you do not have permission to edit this transaction.")
        return redirect('transaction_list')

    form = TransactionForm(request.POST or None, instance=transaction)
    if form.is_valid():
        form.save()
        messages.success(request, "transaction updated successfully.")
        return redirect('transaction_list')

    return render(request, 'budgets/edit_transaction.html', {'form': form})

# view only for staff to see all budgets from all users
@staff_required
def all_budgets(request):
    budgets = Budget.objects.all()
    return render(request, 'budgets/all_budgets.html', {'budgets': budgets})

# a page only visible to staff to restrict access to special tools or info
@staff_required
def admin_only_page(request):
    return render(request, 'budgets/admin_page.html')

print("Budget view accessed")  # debug log