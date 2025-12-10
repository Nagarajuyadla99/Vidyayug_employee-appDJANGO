from django.db import models
from django.core.validators import RegexValidator



phone_validator = RegexValidator(
    regex=r'^\d{10}$',
    message='Phone number must be exactly 10 digits.'
)


class Department(models.Model):
    dep_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.dep_name


class Employees(models.Model):
    
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(
        max_length=10,
        unique=True,
        validators=[phone_validator]
    )
    age = models.IntegerField()
    designation = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    password = models.CharField(max_length=100, default='password123')

    dep = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name