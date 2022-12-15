from django.db import models


# Create your models here.


class Worker(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    street_number = models.PositiveIntegerField()
    bonus_points = models.PositiveIntegerField(default=0)


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    license_plate = models.CharField(max_length=15, unique=True)


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    cars_owned = models.ManyToManyField(Car, blank=True)


class Breakdown(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=1000)
    bonus_points_on_fix = models.PositiveIntegerField()
    urgency = models.PositiveIntegerField()
    is_fixed = models.BooleanField(default=False)
    assigned_worker = models.ForeignKey(Worker, on_delete=models.CASCADE, null=True)
    car_to_repair = models.ForeignKey(Car, on_delete=models.CASCADE, blank=True)


class TestAppointment(models.Model):
    id = models.AutoField(primary_key=True)
    car_to_test = models.ForeignKey(Car, on_delete=models.CASCADE, blank=True)
    bonus_points_on_fix = models.PositiveIntegerField(default=1)
    urgency = models.PositiveIntegerField(default=1)
    assigned_worker = models.ForeignKey(Worker, on_delete=models.CASCADE, null=True, blank=True)
    is_fixed = models.BooleanField(default=False)



