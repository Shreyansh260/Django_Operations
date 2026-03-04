"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *
from Student.views import *

urlpatterns = [
    path('show/',show,name='show'),
    path('search_student/',search_student,name='search_student'),
    path('update/<int:id>/',update,name='update'),
    path('student/',student,name='student'),
    path('about/',about,name='about'),
    path('',home,name = 'home'),
    path('admin/', admin.site.urls),
    path('data1/',data1,name='data1'),
    path('delete/<int:id>/',delete,name='delete'),
    path('login_page/',login_page,name='login_page'),
    path('register/',register,name='register'),
    path('logout_page/',logout_page,name='logout_page'),
]
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)