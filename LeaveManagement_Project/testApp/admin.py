from django.contrib import admin
from testApp.models import *

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display= ['id','name']

class LeaveAdmin(admin.ModelAdmin):
    list_display=['employee', 'date']

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(LeaveRequest, LeaveAdmin)
