from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from testApp.models import *
from testApp.serializers import *

# Create your views here.

def EmployeeView(request):
    return render(request, 'testApp/index.html')
class EmployeeViewSet(ModelViewSet):
    queryset= Employee.objects.all()
    serializer_class= EmployeeSerializer

class LeaveRequestViewSet(ModelViewSet):
    queryset= LeaveRequest.objects.all()
    serializer_class= LeaveRequestSerializer
