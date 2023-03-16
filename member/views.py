from django.shortcuts import render,redirect
from header.models import Addproject,Employee
from leader.models import Assigwork

# Create your views here.

def viewwork(request):
    employee = Assigwork.objects.all()
    return render (request,'view_work.html',{'employee_list':employee})

def viewproject(request):
    employee = Addproject.objects.all()
    return render (request,'viewproject.html',{'employee_list':employee})

def mhome(request):
    return render (request,'member_home.html')

def m_login(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw'] 

        try:
            elogin = Employee.objects.get(e_name=username,e_password=password)
            request.session['e_id']=elogin.id
            return redirect("member:mhome")

        except:
            msg = "invalid username or password"
            
            return render(request,"tlogin.html",{"error_message":msg})
    return render (request,'member_login.html')

def mpsw(request):
    msg = ""
    if request.method == 'POST':
        oldpsw = request.POST['oldpsw']
        newpsw = request.POST['newpsw']
        confirmpwd = request.POST['confirmpsw']

        employee = Employee.objects.get(id =request.session['e_id'])
        if employee.e_password == oldpsw:
            if newpsw == confirmpwd:
                employee.e_password = newpsw
                employee.save()
                msg = "password changed"
            else:
                msg = "password doesnot match"
        else:
            msg ="incorrect password"
    return render (request,'mchange_psw.html',{'status':msg})

def update(request,eid):
    employee = Employee.objects.get(id=eid)
    msg=''

    if request.method=='POST':
        employee.e_name = request.POST['ename']
        employee.e_email = request.POST['eemail']
        employee.e_dob = request.POST['ebirthday']
        employee.e_qualification = request.POST['equlification']
        employee.e_gender = request.POST['egender']
        employee.e_experience = request.POST['experience']
        employee.e_phone = request.POST['phnumber']
        employee.save()
        msg='edited succesfully'
    return render (request,'proupdate.html',{'employee_details':employee,'status':msg})