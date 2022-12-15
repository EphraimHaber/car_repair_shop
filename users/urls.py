from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view),
    path('loginC/', views.LoginView.as_view()),
    path('register/', views.register_view),
    path('registerC/', views.RegisterView.as_view()),
    path('profile/', views.UserView.as_view()),
    path('logout/', views.logout_view, name='log out'),
    path('all/', views.all_users),

]