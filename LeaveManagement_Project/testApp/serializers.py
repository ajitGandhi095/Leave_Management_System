from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from testApp.models import *

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model= Employee
        fields= '__all__'

class LeaveRequestSerializer(ModelSerializer):
    employee_name = serializers.CharField(source='employee.name', read_only=True)
    class Meta:
        model= LeaveRequest
        fields= '__all__'

    def validate(self, data):
        employee= data['employee']
        date= data['date']


        #Check same employee taking leave same date or not
        existing_leave = LeaveRequest.objects.filter(
        employee=employee,
        date=date
        ).exclude(pk=getattr(self.instance, 'pk', None))
        
        if existing_leave.exists():
            raise serializers.ValidationError("Leave already requested for this date")

        month_leave_count= LeaveRequest.objects.filter(
            employee= employee,
            date__year= date.year,
            date__month= date.month
        ).count()

        #check it is an create or update method
        if self.instance:
            original_date= self.instance.date

            if original_date.year == date.year and original_date.month == date.month:
                #No change in month
                return data 
            
        if month_leave_count >=3 :
            raise serializers.ValidationError("Maximum 3 leaves per month allowed")
        
        return data