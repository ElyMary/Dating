from django.db import models

class Employee(models.Model):
    EmpId = models.CharField(max_length=3)
    EmpName = models.CharField(max_length=200)
    EmpGender = models.CharField(max_length=10)
    EmpEmail = models.EmailField()
    EmpDesignation = models.CharField(max_length=150)
    class Meta:
        db_table="Employee"

class TaxPayee(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    # name_of_doctor = models.CharField(max_length=200)
    tin_no = models.IntegerField()
    hospital_name = models.TextField()
    mobile_no = models.IntegerField()
    email_address = models.EmailField()
    class Meta:
        db_table="WitholdingTax"