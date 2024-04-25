from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from adminapp.models import Student, Course
from facultyapp.models import CourseContent

def studenthome(request):
    sid = request.session["sid"]

    student=Student.objects.get(studentid=sid)
    print(student)

    return render(request,"studenthome.html",{"sid":sid,"student":student})

def checkstudentlogin(request):
    sid = request.POST["sid"]
    pwd = request.POST["pwd"]
    flag=Student.objects.filter(Q(studentid=sid)&Q(password=pwd))
    print(flag)
    if flag:
        print("login sucess")
        request.session["sid"] = sid

        student = Student.objects.get(studentid=sid)
        print(student)

        return render(request,"studenthome.html", {"sid":sid, "student":student})
    else:
        msg = "Login Failed"
        return render(request, "studentlogin.html", {"message":msg})
        #return HttpResponse("Login Failed")

def studentchangepwd(request):
    sid = request.session["sid"]
    return render(request, "studentchangepwd.html", {"sid": sid})

def studentupdatepwd(request):
    sid = request.session["sid"]
    opwd=request.POST["opwd"]
    npwd = request.POST["npwd"]
    print(sid,opwd,npwd)

    flag=Student.objects.filter(Q(studentid=sid)&Q(password=opwd))

    if flag:
        print("Old Pwd is Correct")
        Student.objects.filter(studentid=sid).update(password=npwd)
        print("Updated Successfully..!")
        msg = "Password Updated Successfully"
    else:
        print("Old Pwd is Invalid")
        msg = "Old Password is Incorrect"

    return render(request, "studentchangepwd.html", {"sid":sid,"message":msg})

def studentcourses(request):
    sid = request.session["sid"]
    return render(request,"studentcourses.html",{"sid":sid})

def studentcoursecontent(request):
    sid = request.session["sid"]
    #course = get_object_or_404(Course, courseid=cid)
    content = CourseContent.objects.all()#filter(course=course)
    return render(request,"studentcoursecontent.html",{"sid":sid,"coursecontent":content})


def displaystudentcourses(request):
    sid = request.session["sid"]
    ay = request.POST["ay"]
    sem = request.POST["sem"]

    courses = Course.objects.filter(Q(academicyear=ay)&Q(semester=sem))

    return render(request, "displaystudentcourses.html",{"courses":courses,"sid":sid})

def studentcontent(request):
    sid = request.session["sid"]
    return render(request,"studentcontent.html",{"sid":sid})
