from django.urls import path, include
from . import views

urlpatterns = [
    path('addCarTestAppointment/', views.add_car_test_appointment),
    path('getAllTests/', views.get_all_test_appointments),
    path('addBreakdown/', views.add_breakdown),
    path('getAllBreakdowns/', views.get_all_breakdowns),
    path('getAllCars/', views.get_all_cars),
    path('getAllWorkers/', views.get_all_workers),
    path('updateTestAppointment/', views.update_test_appointment),
    path('updateBreakdownFixed/', views.update_breakdown_fixed),
    path('updateTestFixed/', views.update_test_fixed),
    path('getUserDetails/', views.get_user_details)
]
