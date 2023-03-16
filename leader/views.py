from django.shortcuts import render,redirect
from header.models import Employee,Addproject,Addleader
from leader.models import Assigwork

# Create your views here.

def lhome(request):
    return render (request,'leader_home.html')

def tlogin(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw'] 

        try:
            elogin = Employee.objects.get(e_name=username,e_password=password)
            try:
                ledaer=Addleader.objects.get(leader_id=elogin.id)
                request.session['l_id']=ledaer.id
                return redirect("leader:lhome")
            except:
                request.session['e_id']=elogin.id
                return redirect("member:mhome")

        except:
            msg = "invalid username or password"
            
            return render(request,"tlogin.html",{"error_message":msg})
    return render (request,'leader_login.html')

def vteam(request):
    employee = Addproject.objects.all()
    return render (request,'view_team.html',{'employee_list':employee})

def assign(request):
    details=Employee.objects.all()
    if request.method== 'POST':
        works = request.POST['assign']
        
        member = request.POST['ename']
        scid=int(member)
        print(type(scid))
        
        obb=Employee.objects.get(id=scid)
        print(obb)
        

        obj = Assigwork(
                         work_name = works,
                         members_id = obb.id,
                    )
        obj.save()
    return render (request,'assignwork.html',{'det':details})

def cpsw(request):
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
    return render (request,'lchange_psw.html',{'status':msg})

def delt(request):
    employee = Addproject.objects.all()
    return render (request,'delete_employe.html',{'employee_details':employee })


def del_emp(request,eid):
    members = Addproject.objects.get(id = eid)
    employee = Addproject.objects.all()
    print(employee)
    members.delete()
    return redirect('leader:del')
    