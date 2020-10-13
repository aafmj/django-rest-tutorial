from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CalcSerializer


@api_view()
def hello_world(request):
    return Response({"message": "Hello, World"})


@api_view(['GET', 'POST'])
def hello(request):
    if request.method == "GET":
        return Response({"message": "Hello, World"})
    elif request.method == "POST":
        return Response({"message": "Hello, {}".format(request.data["name"])})


# @api_view(['POST'])
# def calculator(request):
#     try:
#         num1 = request.data["num1"]
#         num2 = request.data["num2"]
#         opr = request.data["opr"]
#     except:
#         return Response({"error": "send num1 and num2 and opr"},
#                         status=status.HTTP_400_BAD_REQUEST)
#     else:
#         if isinstance(num1, int) and isinstance(num2, int):
#
#             if opr == "add":
#                 return Response({"result": num1 + num2},
#                                 status=status.HTTP_200_OK)
#             elif opr == "sub":
#                 return Response({"result": num1 - num2},
#                                 status=status.HTTP_200_OK)
#             elif opr == "div":
#                 return Response({"result": num1 / num2},
#                                 status=status.HTTP_200_OK)
#             elif opr == "mul":
#                 return Response({"result": num1 * num2},
#                                 status=status.HTTP_200_OK)
#             else:
#                 return Response({"error": "send a valid opr"},
#                                 status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response({"error": "send integer values"},
#                             status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def calculator(request):
    ser = CalcSerializer(data=request.data)

    if ser.is_valid():
        num1 = ser.data['num1']
        num2 = ser.data['num2']
        opr = ser.data['opr']

        if opr == "add":
            return Response({"result": num1 + num2},
                            status=status.HTTP_200_OK)
        elif opr == "sub":
            return Response({"result": num1 - num2},
                            status=status.HTTP_200_OK)
        elif opr == "div":
            return Response({"result": num1 / num2},
                            status=status.HTTP_200_OK)
        elif opr == "mul":
            return Response({"result": num1 * num2},
                            status=status.HTTP_200_OK)
        else:
            return Response({"error": "send a valid opr"},
                            status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)












