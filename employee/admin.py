from django.contrib import admin
from .models import EmployeeSchema
# For insertion of records through admin panel
admin.site.register(EmployeeSchema)