from django.shortcuts import render
from .models import Students




def index(request):
    return render(request, "index.html")

def add_student(request):

    if request.method == "POST":
        stud_name = request.POST.get("s-name")
        stud_email = request.POST.get("s-email")
        stud_age = request.POST.get("s-age")
        # context = {
        #     "stud_name": stud_name,
        #     "stud_email": stud_email,
        #     "stud_age": stud_age,
        #     "success": "Student list saved successfully"
        # }
        query = Students(name=stud_name, email=stud_email,
                         age=stud_age
                        )
        query.save()

        # return render(request, 'add-student.html', context)
    return render(request, 'add-student.html')

def all_students(request):
    students = Students.objects.all()
    context = {"studentssssssssssssss": students}
    return render(request, 'student.html', context)


