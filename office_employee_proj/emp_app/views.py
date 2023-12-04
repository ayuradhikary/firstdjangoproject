from django.shortcuts import render, HttpResponse
from django.shortcuts import render
from .models import Employee,Role,Department
from datetime import datetime
from django.db.models import Q 

# Create your views here.

def index(req):
    return render(req,'index.html')

def all_emp(req):
    emps = Employee.objects.all()
    context = {
        'employees':emps
    }
    print(context)
    return render(req,'view_all_emp.html',context)

def add_emp(req):
    if req.method == 'POST':
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        salary = int(req.POST['salary'])
        bonus = int(req.POST['bonus'])
        phone = int(req.POST['phone'])
        dept = int(req.POST['dept'])
        role = int(req.POST['role'])
        new_emp = Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept_id=dept,
                 role_id=role,hire_date = datetime.now())
        new_emp.save()
        return HttpResponse('Employee added successfully')
    elif  req.method == 'GET':
        return render(req,'add_emp.html')
    else:
        return HttpResponse("An Exception Occured! Employee Has Not Been Added")

def remove_emp(req, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee removed successfully!")
        except:
            return HttpResponse("Please enter a valid employee id!")
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    print(context)
    return render(req,'remove_emp.html',context)

def filter_emp(req):
    if req.method == 'POST':
        name = req.POST['name']
        dept = req.POST['dept']
        role = req.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)

        context = {
            'emps': emps
        }
        return render(req, 'view_all_emp.html', context)

    elif req.method == 'GET':
        return render(req, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')

