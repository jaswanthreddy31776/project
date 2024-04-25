from django.db.models import Q
from adminapp.models import Faculty, FacultyCourseMapping,Course
from django.shortcuts import render, redirect, get_object_or_404
from .models import CourseContent

def checkfacultylogin(request):
    fid = request.POST["fid"]
    pwd = request.POST["pwd"]
    flag=Faculty.objects.filter(Q(facultyid=fid)&Q(password=pwd))
    print(flag)
    if flag:
        print("login sucess")
        request.session["fid"] = fid
        faculty = Faculty.objects.get(facultyid=fid)
        return render(request,"facultyhome.html", {"fid":fid,"faculty":faculty})
    else:
        msg = "Login Failed"
        return render(request, "facultylogin.html", {"message":msg})
        #return HttpResponse("Login Failed")


def facultyhome(request):
    fid = request.session["fid"]
    print("Faculty ID:", fid)
    faculty = Faculty.objects.get(facultyid=fid)
    print(faculty)

    return render(request, "facultyhome.html",{"fid": fid,"faculty":faculty})


def facultycourses(request):
    fid = request.session["fid"]
    print("Faculty ID:"+fid)

    mappingcourses =FacultyCourseMapping.objects.all()
    fmcourses=[]
    for course in mappingcourses:
        #print(course.faculty.facultyid)
        if(course.faculty.facultyid ==int(fid)):
            fmcourses.append(course)

    print(fmcourses)
    count = len(fmcourses)

    return render(request, "facultycourses.html",{"fid": fid,"fmcourses":fmcourses,"count":count})

def facultychangepwd(request):
    fid = request.session["fid"]
    return render(request, "facultychangepwd.html", {"fid": fid})

def facultyupdatepwd(request):
    fid = request.session["fid"]
    opwd=request.POST["opwd"]
    npwd = request.POST["npwd"]
    print(fid,opwd,npwd)

    flag=Faculty.objects.filter(Q(facultyid=fid)&Q(password=opwd))

    if flag:
        print("Old Pwd is Correct")
        Faculty.objects.filter(facultyid=fid).update(password=npwd)
        print("Updated Successfully..!")
        msg = "Password Updated Successfully"
    else:
        print("Old Pwd is Invalid")
        msg = "Old Password is Incorrect"

    return render(request, "facultychangepwd.html", {"fid":fid,"message":msg})

def facultyviewcontent(request):
    fid = request.session["fid"]
    print(fid)
    content = CourseContent.objects.filter(Q(faculty__facultyid=fid))
    return render(request, 'facultyviewcontent.html',{"fid": fid, "coursecontent": content})




