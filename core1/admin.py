from django.contrib import admin
from .models import Department,Employee

admin.site.register(Department)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=("department","first_name","designation")
    search_fields=['first_name']
    


