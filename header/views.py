from django.shortcuts import render,redirect
from header.models import Hlogin,Employee,Addleader,Addproject,Not

# Create your views here.


def hlogin(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw']

        try:
            hlogin = Hlogin.objects.get(username=username,password=password)
            
            return redirect("header:h_home")
        except:
            msg = "invalid username or password"
            print('niiuwdhiu ')
            return render(request,"hlogin.html",{"error_message":msg})

    return render (request,'hlogin.html')

def h_home(request):
    return render (request,'h_home.html')

def employee(request):
    if request.method== 'POST':
    
        ename = request.POST['ename']
        eemail = request.POST['eemail']
        ebirthday = request.POST['ebirthday']
        equlification = request.POST['equlification']
        egender = request.POST['egender']
        experience = request.POST['experience']
        phnumber = request.POST['phnumber']
        password = request.POST['password']
        obj = Employee(
                        e_name=ename,
                        e_email=eemail,
                        e_dob=ebirthday,
                        e_qualification=equlification,
                        e_experience=experience,
                        e_gender=egender,
                        e_phone=phnumber,
                        e_password=password,

                        )
        obj.save()
    return render (request,'add_employee.html')

def viewemp(request):
    employee = Employee.objects.all()
    return render (request,'view_employee.html',{'employee_list':employee})

def leader(request):
    details=Employee.objects.all()
    if request.method== 'POST':
        tname = request.POST['tname']        
        leader = request.POST['lname']
        scid=int(leader)
        print(type(scid))
        
        obb=Employee.objects.get(id=scid)
        print(obb)
        

        obj = Addleader(
                         team_name = tname,
                         leader_id = obb.id,
                    )
        obj.save()  

    return render (request,'add_tleader.html',{'det':details})

def project(request):
    workers=Employee.objects.all()
    topic=Addleader.objects.all()
    if request.method== 'POST':
        project = request.POST['pname']
        leader = request.POST['lname']
        peoples = request.POST['ename']
       
        efgh = int(leader)
        print(type(efgh))

        abcd = int(peoples)
        print(type(abcd))

        wwe=Addleader.objects.get(id=efgh)
        print(wwe)
        
        wwf=Employee.objects.get(id=abcd)
        print(wwf)
        

        obj = Addproject(
                         p_name = project,
                         leadername_id = wwe.id,
                         employee_id = wwf.id,
                    )
        obj.save()
    return render (request,'add_project.html',{'det':workers,'pro':topic})

def eg(request):
    details=Addleader.objects.all()
    if request.method== 'POST':
        leader = request.POST['lname']
        scid=int(leader)
        print(type(scid))
        
        obb=Addleader.objects.get(id=scid)
        print(obb)
        

        obj = Not(
                         hr_id = obb.id,
                    )
        obj.save()  
    return render (request,'eg.html',{'det':details})