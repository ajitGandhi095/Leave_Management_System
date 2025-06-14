from django.db import models

# Create your models here.

class Employee(models.Model):
    name= models.CharField(max_length=64)

    def __str__(self):
        return self.name

class LeaveRequest(models.Model):
    employee= models.ForeignKey(Employee, on_delete=models.CASCADE)
    date= models.DateField()

    def __str__(self):
        return f"{self.employee.name} - {self.date}"