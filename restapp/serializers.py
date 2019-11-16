from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from restapp.models import Employee

def multiple_of_1000(value):
    if value%1000!=0:
        raise serializers.ValidationError("salary should multiple of 1000")
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'
    def validate_esal(self,value):
        if value<50000:
            raise serializers.ValidationError("Employee salary should be minium 50000")
        return value

    def validate(self,data):
        ename=data.get('ename')
        esal=data.get('esal')
        if ename.lower=='sunny':
            if esal<60000:
                raise serializers.ValidationError("Sunny salary should be minium 60000")
        return data