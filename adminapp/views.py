from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Admin, Faculty, Course, Student, FacultyCourseMapping
from .forms import AddFacultyForm,AddStudentForm, StudentForm, FacultyForm, CourseMappingForm

def adminhome(request):
    auname = request.session["auname"]
    return render(request,"adminhome.html",{"adminuname":auname})

def logout(request):
    return render(request,"login.html")

def checkadminlogin(request):
    adminuname = request.POST["uname"]
    adminpwd = request.POST["pwd"]
    flag=Admin.objects.filter(Q(username=adminuname)&Q(password=adminpwd))
    print(flag)
    if flag:
        print("login sucess")
        request.session["auname"] = adminuname
        return render(request,"adminhome.html", {"adminuname":adminuname})
    else:
        msg = "Login Failed"
        return render(request, "login.html", {"message":msg})
        #return HttpResponse("Login Failed")

def viewstudents(request):
    students=Student.objects.all()
    count = Student.objects.count()
    auname = request.session["auname"]
    return render(request,"viewstudents.html",{"studentdata":students,"count":count,"adminuname": auname})

def viewcourses(request):
    courses = Course.objects.all()
    count = Course.objects.count()
    auname = request.session["auname"]
    return render(request,"viewcourses.html",{"coursesdata":courses,"count":count,"adminuname": auname})

def viewfaculty(request):
    faculty= Faculty.objects.all()
    count = Faculty.objects.count()
    auname = request.session["auname"]
    return render(request,"viewfaculty.html",{"facultydata":faculty,"count":count,"adminuname": auname})

def adminstudent(request):
    auname = request.session ["auname"]
    return render(request,"adminstudent.html",{"adminuname":auname})

def adminfaculty(request):
    auname = request.session["auname"]
    return render(request,"adminfaculty.html",{"adminuname":auname})

def admincourse(request):
    auname = request.session["auname"]
    return render(request,"admincourse.html",{"adminuname":auname})

def addcourses(request):
    auname = request.session["auname"]
    return render(request,"addcourses.html", {"adminuname": auname})

def updatecourse(request):
    auname = request.session["auname"]
    courses = Course.objects.all()
    count = Course.objects.count()
    return render(request, "updatecourse.html", {"adminuname": auname,"courses":courses,"count":count})

def courseupdation(request,cid):
    auname = request.session["auname"]
    return render(request,"courseupdation.html",{"cid":cid,"adminuname": auname})

def courseupdated(request):
    auname = request.session["auname"]

    cid = request.POST["cid"]
    courseid = int(cid)
    dept = request.POST["dept"]
    program = request.POST["program"]
    ay = request.POST["ay"]
    sem = request.POST["sem"]
    year = request.POST["year"]
    ccode = request.POST["ccode"]
    ctitle = request.POST["ctitle"]
    ltps = request.POST["ltps"]
    credits = request.POST["credits"]

    Course.objects.filter(id=courseid).update(department=dept,program=program,academicyear=ay,semester=sem,year=year,coursecode=ccode,coursetitle=ctitle,ltps=ltps,credits=credits)
    msg = "Course Updated Successfully"

    return render(request, "courseupdation.html",{"msg":msg,"adminuname":auname,"cid":cid})

def insertcourse(request):
    auname = request.session["auname"]
    if request.method=="POST":
        dept=request.POST["dept"]
        ay=request.POST["ay"]
        sem=request.POST["sem"]
        year=request.POST["year"]
        ccode=request.POST["ccode"]
        ctitle=request.POST["ctitle"]
        ltps = request.POST["ltps"]
        credits =request.POST["credits"]
        course=Course(department=dept,academicyear=ay,semester=sem,year=year,coursecode=ccode,coursetitle=ctitle,ltps=ltps,credits=credits)
        Course.save(course)
        message ="Course Added Successfully"
    return render(request,"addcourses.html",{"msg": message, "adminuname": auname})

def deletecourse(request):
    courses=Course.objects.all()
    count = Course.objects.count()
    auname = request.session["auname"]
    return render(request,"deletecourse.html",{"coursesdata":courses,"count":count, "adminuname": auname})

def coursedeletion(request,cid):
    Course.objects.filter(id=cid).delete()
    #return HttpResponse("Course deleted Successfully")
    return redirect("deletecourse")

def addfaculty(request):
    auname = request.session["auname"]
    form=AddFacultyForm()
    if request.method=="POST":
        form1=AddFacultyForm(request.POST)
        if form1.is_valid():
            form1.save()
            message="Faculty Added Successfully"
            return render(request,"addfaculty.html",{"msg":message,"form":form, "adminuname": auname})
           # return HttpResponse("Faculty Added Successfully")
        else:
            message = "Failed to Add Faculty"
            return render(request, "addstudent.html", {"msg": message, "form": form, "adminuname": auname})

    return render(request,"addfaculty.html",{"form":form, "adminuname": auname})

def deletefaculty(request):
    faculty=Faculty.objects.all()
    count = Faculty.objects.count()
    auname = request.session["auname"]
    return render(request,"deletefaculty.html",{"facultydata":faculty,"count":count, "adminuname": auname})

def facultydeletion(request,fid):
    Faculty.objects.filter(id=fid).delete()
    #return HttpResponse("Faculty deleted Successfully")
    return redirect("deletefaculty")

def updatefaculty(request):
    auname = request.session["auname"]
    faculty=Faculty.objects.all()
    count = Faculty.objects.count()
    return render(request,"updatefaculty.html",{"facultydata":faculty,"count":count,"adminuname":auname})

def facultyupdation(request, fid):
    print(fid)
    auname = request.session["auname"]
    faculty = get_object_or_404(Faculty, pk=fid)
    if request.method == "POST":
        form = FacultyForm(request.POST, instance=faculty)
        if form.is_valid():
            form.save()
            return redirect('updatefaculty')
        else:
            return HttpResponse("Updation Failed")
    else:
        form = FacultyForm(instance=faculty)
    return render(request, "facultyupdated.html", {"form": form, "adminuname": auname})


def updatestudent(request):
    auname = request.session["auname"]
    student=Student.objects.all()
    count = Student.objects.count()
    return render(request,"updatestudent.html",{"studentdata":student,"count":count,"adminuname":auname})

def studentupdation(request,sid):
    print(sid)
    auname = request.session["auname"]
    student=get_object_or_404(Student,pk=sid)
    if request.method == "POST":
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('updatestudent')
        else:
            return HttpResponse("Updation Failed")
    else:
        form = StudentForm(instance=student)
    return render(request,"studentupdated.html",{"form":form,"adminuname":auname})



def deletestudent(request):
    auname = request.session["auname"]
    student=Student.objects.all()
    count = Student.objects.count()
    return render(request,"deletestudent.html",{"studentdata":student,"count":count,"adminuname":auname})


def studentdeletion(request,sid):
    Student.objects.filter(id=sid).delete()
    #return HttpResponse("Student deleted Successfully")
    return redirect("deletestudent")


def addstudent(request):
    auname = request.session["auname"]
    form=AddStudentForm()
    if request.method=="POST":
        form1=AddStudentForm(request.POST)
        if form1.is_valid():
            form1.save()
            message="Student Added Successfully"
            return render(request,"addstudent.html",{"msg":message,"form":form, "adminuname": auname})
           # return HttpResponse("Faculty Added Successfully")
        else:
            message = "Failed to Add Student"
            return render(request, "addstudent.html", {"msg": message, "form": form, "adminuname": auname})

    return render(request,"addstudent.html",{"form":form, "adminuname":auname})


def facultycoursemapping(request):
    fmcourses = FacultyCourseMapping.objects.all()
    auname = request.session["auname"]
    count = Course.objects.count()
    return render(request, "facultycoursemapping.html", {"adminuname": auname,"count":count,"fmcourses":fmcourses})

def coursemapping(request):
    auname = request.session["auname"]
    form = CourseMappingForm(request.POST, request.FILES)
    if form.is_valid():
        print(form.data)
        form.save()
        return redirect('facultycoursemapping')
    else:
        form = CourseMappingForm()
    return render(request, 'coursemapping.html', {"adminuname": auname,"form": form})

def adminchangepwd(request):
    auname = request.session["auname"]
    return render(request, "adminchangepwd.html", {"adminuname": auname})

def adminupdatepwd(request):
    auname = request.session["auname"]
    opwd=request.POST["opwd"]
    npwd = request.POST["npwd"]
    print(auname,opwd,npwd)

    flag=Admin.objects.filter(Q(username=auname)&Q(password=opwd))

    if flag:
        print("Old Pwd is Correct")
        Admin.objects.filter(username=auname).update(password=npwd)
        print("Updated Successfully..!")
        msg = "Password Updated Successfully"
    else:
        print("Old Pwd is Invalid")
        msg = "Old Password is Incorrect"

    return render(request, "adminchangepwd.html", {"adminuname":auname,"message":msg})

