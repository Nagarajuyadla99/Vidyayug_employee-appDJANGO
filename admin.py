from django.contrib import admin
from .models import Employees, Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dep_name',)

@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'designation', 'dep', 'date_of_joining')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('dep',)
