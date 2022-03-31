from django.db import models


# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=100)
    mob = models.CharField(max_length=20, unique=True)
    Address = models.CharField(max_length=300)
    Email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)


class Workers(models.Model):
    name = models.CharField(max_length=100)
    mob = models.CharField(max_length=20, unique=True)
    Address = models.CharField(max_length=300)
    Email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    work = models.CharField(max_length=100)
    charges = models.CharField(max_length=100)
    rating = models.IntegerField()


class Appointment(models.Model):
    worker_id = models.ForeignKey(Workers, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    Appointment_date = models.CharField(max_length=300)
    completed = models.IntegerField(default=0)
