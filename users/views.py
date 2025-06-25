from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import UserRegisterForm
from budgets.models import Transaction, Budget

# handles user registration using a custom form
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # create a new user account
            messages.success(request, 'account created successfully.')
            return redirect('login')  # redirect to login page after success
    else:
        form = UserRegisterForm()  # show a blank form for get requests
    return render(request, 'users/register.html', {'form': form})

# handles user login using username and password
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)  # check if credentials are valid
        if user:
            login(request, user)  # log the user in
            return redirect('dashboard')  # go to dashboard on success
        else:
            messages.error(request, 'invalid credentials')  # show error if login fails
    return render(request, 'users/login.html')

# logs the user out and redirects to login page
def logout_view(request):
    logout(request)
    return redirect('login')

# public landing page (optional)
def home(request):
    return render(request, 'users/home.html')

# shows the user's dashboard with recent transactions and budgets
@login_required
def dashboard_view(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')[:5]  # get latest 5 transactions
    budgets = Budget.objects.filter(user=request.user).order_by('-date')[:5]  # get latest 5 budgets
    return render(request, 'users/dashboard.html', {
        'transactions': transactions,
        'budgets': budgets
    })
