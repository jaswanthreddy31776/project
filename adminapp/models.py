from django.db import models

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,blank=False,unique=True)
    password=models.CharField(max_length=100,blank=False)
    class Meta:
        db_table="admin_table"
    def __str__(self):
        return str(self.id)


class Course(models.Model):
    id=models.AutoField(primary_key=True)
    department_choices=(("CSE(Regular)","CSE(R)"),("CSE(Honors)","CSE(H)"),("CSE&IT","CSEIT") )
    department=models.CharField(max_length=100,blank=False,choices=department_choices)

    academic_choices=(("2023-24","2023-24"),("2022-23","2022-23"),("2021-22","2021-22") )

    academicyear = models.CharField(max_length=20,blank=False,choices=academic_choices)

    sem_choices=(("ODD","ODD"),("EVEN","EVEN"))
    semester=models.CharField(max_length=20,blank=False,choices=sem_choices)
    year=models.IntegerField(blank=False)
    coursecode = models.CharField(max_length=20, blank=False)
    coursetitle = models.CharField(max_length=100, blank=False)
    ltps = models.CharField(max_length=10,blank=False)
    credits = models.FloatField(blank=False)

    class Meta:
        db_table="course_table"
    def __str__(self):
         return str(self.coursecode)

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    studentid=models.BigIntegerField(blank=False,unique=True)
    fullname=models.CharField(max_length=100,blank=False)
    gender_choices=(("MALE","MALE"),("FEMALE","FEMALE"))
    gender=models.CharField(max_length=50,blank=False,choices=gender_choices)
    department_choices=(("CSE(Regular)","CSE(R)"),("CSE(Honors)","CSE(H)"),("CSE&IT","CSEIT") )
    department = models.CharField(max_length=100, blank=False,choices=department_choices)
    program_choices=(("B.Tech" ,"B.Tech"),("M.Tech","M.Tech"),("CSE&IT","CSEIT") )
    program = models.CharField(max_length=100, blank=False,choices=program_choices)
    sem_choices=(("ODD","ODD"),("EVEN","EVEN"))

    semester = models.CharField(max_length=20, blank=False,choices=sem_choices)

    year = models.IntegerField(blank=False)
    password = models.CharField(max_length=100, blank=False,default="klu123")
    email = models.CharField(max_length=100, blank=False,unique=True)
    contact = models.CharField(max_length=20, blank=False,unique=True)
    class Meta:
        db_table="student_table"
    def __str__(self):
        return str(self.studentid)

class Faculty(models.Model):
    id = models.AutoField(primary_key=True)
    facultyid=models.BigIntegerField(blank=False,unique=True)
    fullname=models.CharField(max_length=100,blank=False)
    gender_choices=(("MALE","MALE"),("FEMALE","FEMALE"))
    gender=models.CharField(max_length=50,blank=False,choices=gender_choices)
    department_choices=(("CSE(Regular)","CSE(R)"),("CSE(Honors)","CSE(H)"),("CSE&IT","CSEIT") )

    department = models.CharField(max_length=100, blank=False,choices=department_choices)
    qualification_choices=(("M.Tech","M.Tech"),("Phd","Phd") )

    qualification = models.CharField(max_length=100, blank=False,choices=qualification_choices)
    desihnation_choices=(("Prof.","Professor"),("Assoc.Prof","Associate Professor"),("Assit.Prof","Assitant Professor") )

    designation = models.CharField(max_length=100, blank=False,choices=desihnation_choices)
    password = models.CharField(max_length=100, blank=False,default="klu123")
    email = models.CharField(max_length=100, blank=False,unique=True)
    contact = models.CharField(max_length=20, blank=False,unique=True)

    class Meta:
        db_table="faculty_table"


    def __str__(self):
        return str(self.facultyid)

class FacultyCourseMapping(models.Model):
    mappingid = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    components_choices = (("L","Lecture"),("T","Tutorial"),("P","Practical"),("S","Skill"))
    component = models.CharField(max_length=10,blank=False,choices=components_choices)

    type = models.BooleanField(blank=False, verbose_name="Faculty Type")
    section = models.IntegerField(blank=False)

    class Meta:
        db_table = "facultycoursemapping_table"

    def __str__(self):
        return f"{self.course.coursetitle}-{self.faculty.fullname}"