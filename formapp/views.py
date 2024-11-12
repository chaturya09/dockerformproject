# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages  
from .forms import EmployeeForm
from .models import Employee


def employee_list(request):
    employees = Employee.objects.all()  
    return render(request, 'employee_list.html', {'employees': employees})


def inputview(request, id=None):
    if id:  
        employee = get_object_or_404(Employee, empid=id)  
        if request.method == 'POST':
            form = EmployeeForm(request.POST, instance=employee)  
            if form.is_valid(): 
                form.save()  
                messages.success(request, 'Employee updated successfully!')
                return redirect('employee_list')  
            else:
                print("Form is not valid:", form.errors)  
        else:
            form = EmployeeForm(instance=employee)  
    else:  
        if request.method == 'POST':
            form = EmployeeForm(request.POST)  
            if form.is_valid():  
                form.save() 
                messages.success(request, 'Employee created successfully!')
                return redirect('employee_list')  
            else:
                print("Form is not valid:", form.errors)  
        else:
            form = EmployeeForm()  

    return render(request, 'input.html', {'empform': form})  


def delete_employee(request, id):
    employee = get_object_or_404(Employee, empid=id) 
    if request.method == 'POST':
        employee.delete()  
        messages.success(request, 'Employee deleted successfully!')
        return redirect('employee_list')  
    return render(request, 'confirm_delete.html', {'employee': employee})  










