from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')
    

def about(request):
    print("About page is opened")
    return HttpResponse("<h1>This is the about page.</h1>")
def data1(request):
    data = [{
        'name': 'John Doe',
        'age': 30,
        'city': 'New York'
    }, 
    {
        'name': 'Jane Smith',
        'age': 25,
        'city': 'Los Angeles'
    },
    {
        'name': 'Alice Johnson',
        'age': 28,  
        'city': 'Chicago'
    },
    {
        'name': 'Bob Brown',
        'age': 35,
        'city': 'Houston'
    },
    {
        'name': 'Charlie Davis',
        'age': 22,  
        'city': 'Phoenix'
    }]

    return render(request,'index.html',context={'data1': data})
   