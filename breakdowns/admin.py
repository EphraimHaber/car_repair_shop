from django.contrib import admin
from .models import Car, Customer, TestAppointment, Worker, Breakdown
admin.site.register(Car)
admin.site.register(Customer)
admin.site.register(TestAppointment)
admin.site.register(Worker)
admin.site.register(Breakdown)

# Register your models here.
