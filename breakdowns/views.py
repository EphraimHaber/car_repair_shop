import jwt
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django.shortcuts import get_object_or_404

from .models import TestAppointment, Breakdown, Car, Worker
from .serializers import TestAppointmentSerializer, BreakdownSerializer, CarSerializer, WorkerSerializer


# Create your views here.
@api_view(["POST"])
# @permission_classes((IsAuthenticated,))
def add_car_test_appointment(request: HttpRequest):
    response = Response()
    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed('Unauthenticated!')
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')

    object_data = JSONParser().parse(request)
    data_serialized = TestAppointmentSerializer(data=object_data)
    if data_serialized.is_valid():
        instance = data_serialized.create(data_serialized.data)
        instance.car_to_test = Car.objects.filter(id=object_data['car_to_test']).first()
        try:
            instance.assigned_worker = Worker.objects.filter(id=object_data['assigned_worker']).first()
        except KeyError:
            instance.assigned_worker = None
        instance.save()
        response.data = {'message': 'success'}
        return response
    print(data_serialized.errors)
    response.data = {'message': data_serialized.errors}
    return response


@api_view(["PUT"])
def update_test_appointment(request):
    response = Response()
    object_data = JSONParser().parse(request)
    data_serialized = TestAppointmentSerializer(data=object_data)
    try:
        instance_to_update = get_object_or_404(TestAppointment, id=object_data['id'])
    except KeyError:
        response.data = {'message': 'nope'}
        return response
    if data_serialized.is_valid():
        try:
            object_data['car_to_test'] = Car.objects.filter(id=object_data['car_to_test']).first()
            object_data['assigned_worker'] = Worker.objects.filter(id=object_data['assigned_worker']).first()
            # print(object_data['assigned_worker'])
        except KeyError:
            response.data = {'message': 'nope'}
            return response
        data_serialized.update(instance_to_update, object_data)
        response.data = {'message': 'good'}
        return response
    response.data = {'message': 'nope'}
    return response


@api_view(["PUT"])
def update_breakdown_fixed(request):
    response = Response()
    object_data = JSONParser().parse(request)
    data_serialized = BreakdownSerializer(data=object_data)
    try:
        instance_to_update = get_object_or_404(Breakdown, id=object_data['id'])
    except KeyError:
        response.data = {'message': 'nope'}
        return response
    if data_serialized.is_valid():
        try:
            object_data['car_to_repair'] = Car.objects.filter(id=object_data['car_to_repair']).first()
            object_data['assigned_worker'] = Worker.objects.filter(id=object_data['assigned_worker']).first()
        except KeyError:
            response.data = {'message': 'nope'}
            return response
        data_serialized.update(instance_to_update, object_data)
        response.data = {'message': 'good'}
        return response
    response.data = {'message': 'nope'}
    return response


@api_view(["PUT"])
def update_test_fixed(request):
    response = Response()
    object_data = JSONParser().parse(request)
    data_serialized = TestAppointmentSerializer(data=object_data)
    try:
        instance_to_update = get_object_or_404(TestAppointment, id=object_data['id'])
        if data_serialized.is_valid():
            object_data['car_to_test'] = Car.objects.filter(id=object_data['car_to_test']).first()
            object_data['assigned_worker'] = Worker.objects.filter(id=object_data['assigned_worker']).first()
            data_serialized.update(instance_to_update, object_data)
            response.data = {'message': 'good'}
            return response
    except KeyError:
        response.data = {'message': 'nope, key error'}
        return response
    response.data = {'message': 'nope'}
    return response


@api_view(["GET"])
# @permission_classes((IsAuthenticated,))
def get_all_test_appointments(request):
    # token = request.COOKIES.get('jwt')
    # if not token:
    #     raise AuthenticationFailed('Unauthenticated!')
    # try:
    #     payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    # except jwt.ExpiredSignatureError:
    #     raise AuthenticationFailed('Unauthenticated!')

    # todo allow only is user is staff - problem: ImportError: attempted relative import beyond top-level package
    # user = User.objects.filter(id=payload['id']).first()
    # if not user['is_staff']:
    #     raise AuthenticationFailed('You lack permission to invoke this operation.')
    data = TestAppointment.objects.all()
    deserialized_data = TestAppointmentSerializer(data, many=True)
    return Response(deserialized_data.data, status=HTTP_200_OK)


@api_view(["POST"])
# @permission_classes((IsAuthenticated,))
def add_breakdown(request):
    response = Response()
    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed('Unauthenticated!')
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')
    object_data = JSONParser().parse(request)
    data_serialized = BreakdownSerializer(data=object_data)
    if data_serialized.is_valid():
        instance = data_serialized.create(data_serialized.data)
        instance.car_to_repair = Car.objects.filter(id=object_data['car_to_repair']).first()
        try:
            instance.assigned_worker = Worker.objects.filter(id=object_data['assigned_worker']).first()
        except KeyError:
            instance.assigned_worker = None
        instance.save()
        response.data = {'message': 'success'}
        return response
    response.data = {'message': 'fail'}
    return Response


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_workers_bonus_points(request):
    pass


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def update_breakdown_status(request):
    pass


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_breakdown_info(request):
    pass


@api_view(["GET"])
# @permission_classes((IsAuthenticated,))
def get_all_breakdowns(request):
    # token = request.COOKIES.get('jwt')
    # if not token:
    #     raise AuthenticationFailed('Unauthenticated!')
    # try:
    #     payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    # except jwt.ExpiredSignatureError:
    #     raise AuthenticationFailed('Unauthenticated!')
    data = Breakdown.objects.all()
    deserialized_data = BreakdownSerializer(data, many=True)
    return Response(deserialized_data.data, status=HTTP_200_OK)


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_bonus_points(request):
    pass


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_peer_comparison(request):
    pass


@api_view(["POST"])
# @permission_classes((IsAuthenticated,))
def get_all_cars(request):
    # token = request.COOKIES.get('jwt')
    # if not token:
    #     raise AuthenticationFailed('Unauthenticated!')
    # try:
    #     payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    # except jwt.ExpiredSignatureError:
    #     raise AuthenticationFailed('Unauthenticated!')
    data = Car.objects.all()
    deserialized_data = CarSerializer(data, many=True)
    return Response(deserialized_data.data, status=HTTP_200_OK)


@api_view(["GET"])
# @permission_classes((IsAuthenticated,))
def get_all_workers(request):
    # token = request.COOKIES.get('jwt')
    # if not token:
    #     raise AuthenticationFailed('Unauthenticated!')
    # try:
    #     payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    # except jwt.ExpiredSignatureError:
    #     raise AuthenticationFailed('Unauthenticated!')
    data = Worker.objects.all()
    deserialized_data = WorkerSerializer(data, many=True)
    return Response(deserialized_data.data, status=HTTP_200_OK)
