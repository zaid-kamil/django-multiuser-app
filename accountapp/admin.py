from django.contrib import admin
from .models import CustomerProfile, EmployeeProfile, ManagerProfile

admin.site.register(CustomerProfile)
admin.site.register(EmployeeProfile)
admin.site.register(ManagerProfile)