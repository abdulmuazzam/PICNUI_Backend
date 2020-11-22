from django.shortcuts import render

from rest_framework import response, decorators, permissions, status
from .serializers import RoutineSerializer
from rest_framework.response import Response
from .models import Routine
# Create your views here.

@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def Add_Routine_API(request):
    print('Test Post API: ', request.POST.get('option'))
    serializer = RoutineSerializer(data=request.data)
    print(serializer.is_valid())
    if serializer.is_valid():
        print("before Save")
        serializer.save()
        print(serializer.data)


        data = {'routine': serializer.data}
        print("Response routine is ", data)
        return Response(data, status=status.HTTP_200_OK)

        # return Response(serializer.data, status=status.HTTP_201_CREATED)
    print("error")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@decorators.api_view(["GET"])
@decorators.permission_classes([permissions.AllowAny])
def Get_All_Routines_API(request):
    routine = Routine.objects.all()
    serializer = RoutineSerializer(routine, many=True)
    return Response(serializer.data)