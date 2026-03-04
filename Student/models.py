from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    name = models.CharField(max_length=255)
    student_class = models.CharField(max_length=255)
    age = models.IntegerField()
    image = models.ImageField(upload_to='student_images/')
    
    def __str__(self):
        return self.name


