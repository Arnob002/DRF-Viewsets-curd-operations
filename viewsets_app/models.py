from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    emp_id = models.CharField(max_length=20,null=True)
    emp_name = models.CharField(max_length=50,null=True)
    emp_address = models.TextField(null=True)

    def __str__(self):
        return f'{self.emp_name}'
