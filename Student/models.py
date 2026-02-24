from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    student_class = models.CharField(max_length=255)
    age = models.IntegerField()
    image = models.ImageField(upload_to='student_images/')
    def __str__(self):
        return self.name


