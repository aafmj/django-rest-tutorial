from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets, permissions

from .models import Person, Car
from .serializers import PersonSerializer, CarSerializer, CarReadSerializer


# @api_view(['GET', 'POST'])
# def person_view(request):
#     if request.method == "GET":
#         person = Person.objects.all()
#         return Response(PersonSerializer(person, many=True).data,
#                       status=status.HTTP_200_OK)
#
#     elif request.method == "POST":
#         ser = PersonSerializer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    search_fields = ('name', )
    ordering_fields = '__all__'

    def list(self, request, *args, **kwargs):
        objs = super().list(request, *args, **kwargs)
        print("---- List ----")
        return objs

    def create(self, request, *args, **kwargs):
        obj = super().create(request, *args, **kwargs)
        print("---- Create ----")
        return obj

    def update(self, request, *args, **kwargs):
        obj = super().update(request, *args, **kwargs)
        instance = self.get_object()
        print("---- Update : {}".format(instance.name))
        return obj

    def retrieve(self, request, *args, **kwargs):
        obj = super().retrieve(request, *args, **kwargs)
        instance = self.get_object()
        print("---- Retrieve : {}".format(instance.name))
        return obj

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print("---- Destroy : {}".format(instance.name))
        obj = super().destroy(request, *args, **kwargs)
        return obj


# @api_view(['GET', 'POST'])
# def car_view(request):
#     if request.method == "GET":
#         car = Car.objects.all()
#         return Response(CarSerializer(car, many=True).data,
#                       status=status.HTTP_200_OK)
#
#     elif request.method == "POST":
#         ser = CarSerializer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET'])
# def information_view(request):
#     car = Car.objects.all()
#     return Response(CarReadSerializer(car, many=True).data,
#                     status=status.HTTP_200_OK)

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_serializer_class(self):
        if not self.request.method not in permissions.SAFE_METHODS:
            return CarSerializer
        else:
            return CarReadSerializer













