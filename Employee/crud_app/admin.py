from django.contrib import admin
from .models import Employee
from import_export.admin import ImportExportModelAdmin
from .models import TaxPayee



admin.site.register(Employee)

@admin.register(TaxPayee)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'middle_name', 'tin_no', 'hospital_name', 'mobile_no', 'email_address')