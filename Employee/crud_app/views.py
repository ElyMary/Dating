from django.shortcuts import render, redirect
from .models import Employee
from .models import TaxPayee
from .resources import TaxPayeeResource
from django.contrib import messages
from tablib import Dataset 


# Create Employee

def insert_emp(request):
    if request.method == "POST":
        EmpId = request.POST['EmpId']
        EmpName = request.POST['EmpName']
        EmpGender = request.POST['EmpGender']
        EmpEmail = request.POST['EmpEmail']
        EmpDesignation = request.POST['EmpDesignation']
        data = Employee(EmpId=EmpId, EmpName=EmpName, EmpGender=EmpGender, EmpEmail=EmpEmail, EmpDesignation= EmpDesignation)
        data.save()
  
        return redirect('show/')
    else:
        return render(request, 'insert.html')

# Retrive Employee
        
def show_emp(request):
    employees = Employee.objects.all()
    return render(request,'show.html',{'employees':employees} )

# Update Employee

def edit_emp(request,pk):
    employees = Employee.objects.get(id=pk)
    if request.method == 'POST':
            print(request.POST)
            employees.EmpName = request.POST['EmpName']
            employees.EmpGender = request.POST['EmpGender']
            employees.EmpEmail = request.POST['EmpEmail']
            employees.EmpDesignation = request.POST['EmpDesignation']
            employees.EmpDesignation = request.POST['EmpDesignation']
            employees.save()   
            return redirect('/show')
    context = {
        'employees': employees,
    }

    return render(request,'edit.html',context)


# Remove/Delete Employee
def remove_emp(request, pk):
    employees = Employee.objects.get(id=pk)

    if request.method == 'POST':
        employees.delete()
        return redirect('/show')

    context = {
        'employees': employees,
    }

    return render(request, 'delete.html', context)

# bulk upload
def bulkupload(request):
    if request.method == 'POST':
        taxpayee_resource = TaxPayeeResource()  # Updated to use TaxPayeeResource
        dataset = taxpayee_resource.load(new_taxpeyee.read(), format='xlsx')
        new_taxpeyee = request.FILES['myfile']

        if not new_taxpeyee.name.endswith('xlsx'):
            messages.info(request, 'Wrong Format')
            return render(request, 'bulkupload.html')
        
        imported_data = dataset.load(new_taxpeyee.read(), format='xlsx')
        for data in imported_data:
            # Unpack values from the data list
            id, last_name, first_name, middle_name, tin_no, hospital_name, mobile_no, email_address = data

            # Create a TaxPayee object with the unpacked values
            taxpeyee = TaxPayee(
                id=id,
                last_name=last_name,
                first_name=first_name,
                middle_name=middle_name,
                tin_no=tin_no,
                hospital_name=hospital_name,
                mobile_no=mobile_no,
                email_address=email_address
            )

            # Save the TaxPayee object to the database
            taxpeyee.save()

        return redirect('show/')
    else:
        return render(request, 'bulkupload.html')
