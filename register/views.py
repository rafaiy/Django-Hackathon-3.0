from django.views.generic import ListView, View, CreateView
from register.models import *


class Adduser(CreateView):
    model = user
    fields = ['name', 'Fname', 'mobile', 'aadharno', 'yob', 'gender', 'address', 'pincode','password']







