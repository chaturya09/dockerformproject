from django.db import models

class Employee(models.Model):
    empid = models.IntegerField(primary_key=True)  
    empname = models.CharField(max_length=100)
    empage = models.IntegerField(null=True, blank=True)
    empsal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    def __str__(self):
        return self.empname








