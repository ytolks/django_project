import re
from django.shortcuts import redirect, render
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST': #form submittion
        messages.error(request, 'Testing error message')
       #register user
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST': #form submittion
       #login user
       return
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')