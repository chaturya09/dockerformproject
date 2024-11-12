from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('empid', 'empname', 'empage', 'empsal')  # Display fields
