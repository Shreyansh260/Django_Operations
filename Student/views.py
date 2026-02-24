from django.shortcuts import render,redirect
from Student.models import *

def student(request):
   if request.method == 'POST':
    data = request.POST
    image = request.FILES.get('image')
    name = request.POST.get('name')  # we can aslo use data.get('name') instead of request.POST.get('name')
    student_class = request.POST.get('student_class')
    age = request.POST.get('age')
    """print(image)
    print(name)
    print(student_class)
    print(age)

    print(f"This is the data: \n {data}")"""

    Student.objects.create(name = name ,
                           student_class = student_class,
                           age = age,
                           image = image)
    return redirect('show')
    
   return render(request,'first.html')

def show(request):
    quries = Student.objects.all()
    context = {'show': quries}
    return render(request,'show.html',context=context)
