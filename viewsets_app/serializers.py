from rest_framework import serializers
from .models import *

class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = '__all__'