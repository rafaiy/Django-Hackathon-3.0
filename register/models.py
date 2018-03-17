from django.db import models
from django.shortcuts import reverse


class user(models.Model):
    name = models.CharField(max_length=20)
    Fname = models.CharField(max_length=20)
    mobile = models.IntegerField()
    Email = models.CharField(max_length=20)
    aadharno = models.IntegerField(primary_key=True)
    yob = models.DateField()
    gender = models.CharField(max_length=6)
    address = models.CharField(max_length=30)
    pincode = models.IntegerField()
    password = models.CharField(max_length=10)
    securityquestion = models.CharField(max_length=20)
    answer = models.CharField(max_length=10)

    def get_absolute_url(self):
        return reverse('login')

    def __str__(self):
        return self.type




