from rest_framework import serializers 
from .models import EmployeeSchema

class EmployeeSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = EmployeeSchema
        fields = '__all__'