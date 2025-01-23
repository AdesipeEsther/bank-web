from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *

import random

def generate_account_number(length=10):
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    return ''.join(random.choices(numbers, k=length))

#4119494912
def transfer(request):
    user_account = request.user.account
    if request.method == "POST":
        acct_no = request.POST.get("account")
        receiver_account = Account.objects.get(account_no=acct_no)
        amount = float(request.POST.get("amount"))
        print(amount)
        if user_account.account_balance < int(amount):
            messages.warning(request, "Sapa dey your account")  # recorded
            return redirect("home")
        user_account.account_balance -= amount
        receiver_account.account_balance += amount
        user_account.save()
        receiver_account.save()
        transaction = Transaction.objects.create(sender=user_account, amount=amount, receiver=receiver_account)
    return redirect("home")

def home(request):
    user = request.user
    if user.is_authenticated:
        transaction_history = Transaction.objects.filter(sender=user.account)
        context = {
            "transactions":transaction_history
        }
    else:
        context = {}
    return render(request, "home.html", context)

def about(request):
    return render(request, "about.html", {})

def terms(request):
    return render(request, "terms.html", {})

def privacy(request):
    return render(request, "privacy.html", {})

def login_page(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('login')

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        age = request.POST.get('age')
        # if age < 18:
        #     childaccount = 
        if form.is_valid():
            user = form.save(commit=False)
            user_profile = Account(user=user, account_no=generate_account_number())
            user.save()
            user_profile.save()
            return redirect('login')
    context = {
        "form":form
    }
    return render(request, 'register.html', context)