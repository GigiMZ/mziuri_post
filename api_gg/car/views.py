from django.contrib.admindocs.views import BookmarkletsView
from django.core.serializers import serialize
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Car
from django.forms import model_to_dict
from .serialaizer import CarSerialaizer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def index(request):
    if request.method == 'GET':
        cars = Car.objects.all()
        serialaizer = CarSerialaizer(cars)
        return Response(serialaizer.data)

    if request.method == 'POST':
        serializer = CarSerialaizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Successful!"}, status=status.HTTP_201_CREATED)
