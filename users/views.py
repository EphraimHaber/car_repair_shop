from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
import datetime
import jwt
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import UserSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

User = get_user_model()


# Create your views here.
def home(request):
    return render(request, "authentication/index.html")


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@permission_classes((AllowAny,))
class LoginView(APIView):
    def post(self, request):
        print(request.data)
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        # token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        # user = authenticate(username=username, password=pass1)
        user = User.objects.filter(username=username).first()
        temp = user.password
        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(pass1):
            raise AuthenticationFailed(f'Incorrect password! {temp}')

        if user is not None:
            login(request, user)
            return render(request, "authentication/index.html", {"fname": username})

        messages.error(request, f"Bad Credentials!! {user}")
    return render(request, "authentication/signin.html")


def register_view(request: HttpRequest):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')

        if len(username) > 20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')

        my_user = User.objects.create_user(username, email, pass1)
        my_user.first_name = fname
        my_user.last_name = lname
        my_user.is_active = True
        my_user.save()
        messages.success(request, "Your Account has been created successfully!! .")
        return render(request, "authentication/signin.html")

    return render(request, "authentication/signup.html")


def profile_view(request: HttpRequest):
    return HttpResponse('<h1>profile view</h1>')


def logout_view(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')


def all_users(request):
    if request.user.is_authenticated:
        temp = list(User.objects.filter(is_superuser=True))
        for i in range(len(temp)):
            if temp[i] == request.user:
                entries_list = list(User.objects.values())
                return JsonResponse(entries_list, safe=False)
    return HttpResponse("<p>You do not have permission to view this file</p>")
