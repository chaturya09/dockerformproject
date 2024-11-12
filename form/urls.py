from django.urls import path
from formapp import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.employee_list, name='employee_list'),
    path('employee/<int:id>/', views.inputview, name='update_employee'),  # Update employee
    path('employee/delete/<int:id>/', views.delete_employee, name='delete_employee'),  # Delete employee
    path('employee/create/', views.inputview, name='create_employee'),  # Create employee
]





