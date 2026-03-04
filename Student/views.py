from django.shortcuts import render,redirect
from Student.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login_page')

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

@login_required(login_url='login_page')
def show(request):
    quries = Student.objects.all()
    context = {'show': quries}
    return render(request,'show.html',context=context)

def delete(request,id):
      Student.objects.get(id=id).delete()
      return redirect('show')

def update(request,id):
    quries = Student.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        name = data.get('name')  # we can aslo use data.get('name') instead of request.POST.get('name')
        student_class = data.get('student_class')
        age = data.get('age')


        quries.name = name
        quries.student_class = student_class
        quries.age = age
        if image:
            quries.image = image
        quries.save()
        return redirect('show')
    
    
    context = {'up': quries}
    return render(request,'update.html',context=context)

def search_student(request):
    search = request.GET.get('search')

    if search:
        students = Student.objects.filter(name__icontains=search)
    else:
        students = Student.objects.all()

    context = {'show': students}
    return render(request, 'show.html', context)
    
def login_page(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid username")
            return redirect('login_page')
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Invalid password")
            return redirect('login_page')
        
        else:
            login(request, user)
            return redirect('show')
    
    
    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('login_page')

def register(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        password = data.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request, 'Username already exists. Please choose a different username.')
            return redirect('register')

        user = User.objects.create(username=username,
                                        first_name=first_name,
                                        last_name=last_name)
        user.set_password(password)
        user.save()
        # No need to set password separately when using create_user, it handles password hashing internally.

        messages.info(request, 'Registration successful. You can now log in.')

        return redirect('login_page')


    return render(request,'register.html')