from django.shortcuts import render,get_object_or_404
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status


# Create your views here.

# # viewsets.viesset 
# class employeeViewSet(viewsets.ViewSet):
#     def list(self, request):
#         quaryset = EmployeeModel.objects.all()
#         serializers = employeeSerializer(quaryset, many=True)
#         return Response(serializers.data)

#     def create(self,request):
#         serializers = employeeSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data,status=status.HTTP_201_CREATED)
#         return Response(serializers.errors)

#     # single object view sets: 
#     def retrieve(self, request, pk=None):
#         employee = get_object_or_404(EmployeeModel,pk = pk)
#         serializers = employeeSerializer(employee)
#         return Response(serializers.data,status=status.HTTP_200_OK)

#     def update(self, request, pk=None):
#         employee = get_object_or_404(EmployeeModel,pk = pk)
#         serializers = employeeSerializer(employee, data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data,status=status.HTTP_201_CREATED)
#         return Response(serializers.errors,status=status.HTTP_404_NOT_FOUND)

#     def delete(self, request, pk=None):
#         employee = get_object_or_404(EmployeeModel, pk = pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

    
# viewsets.modelviewset

class employeeViewSet(viewsets.ModelViewSet):
    queryset = EmployeeModel.objects.all()
    serializer_class = employeeSerializer    
