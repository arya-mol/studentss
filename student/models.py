from django.db import models

# Create your models here.

class Grade(models.Model):
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.code

class Student(models.Model):
    name=models.CharField(max_length=120)
    address=models.CharField(max_length=120)
    email=models.EmailField(unique=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    def __str__(self):
        return self.name





