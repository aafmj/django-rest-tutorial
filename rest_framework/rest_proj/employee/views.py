from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Employee
from .serializers import EmployeeSerializer


@api_view(['POST'])
def post_employee(request):
    data = {
        'name': request.data['name'],
        'age': request.data['age'],
        'salary': request.data['salary'],
        'post': request.data['post']
    }

    ser = EmployeeSerializer(data=data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)
    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_employees(request):
    employees = Employee.objects.all()
    ser = EmployeeSerializer(employees, many=True)
    return Response(ser.data, status=status.HTTP_200_OK)


@api_view(['PUT', 'GET', 'DELETE'])
def get_update_delete_employee(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except:
        return Response({"error": "Not Found!"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        ser = EmployeeSerializer(employee)
        return Response(ser.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        ser = EmployeeSerializer(employee, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def search_employee(request):
    employees = Employee.objects.filter(name=request.query_params['name'])

    if employees:
        ser = EmployeeSerializer(employees, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
