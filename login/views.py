from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def Login(request):

    return render(request, template_name= 'login/login.html')
