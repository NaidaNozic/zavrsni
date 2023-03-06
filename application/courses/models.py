from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class NewUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_tutor = models.BooleanField(default=False)

class Course(models.Model):
    name = models.CharField(max_length=250)
    summary = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(NewUser,on_delete=models.CASCADE,primary_key=True,related_name='Student')
    phone = models.IntegerField()
    age = models.IntegerField(null=True,blank=True) #this field is optional
    course = models.ManyToManyField(Course,through="StudentCourse")

    def __str__(self):
        return self.user.first_name+' '+self.user.last_name

class Tutor(models.Model):
    user = models.OneToOneField(NewUser,on_delete=models.CASCADE,primary_key=True,related_name='Tutor')
    phone = models.IntegerField()
    course = models.ManyToManyField(Course,through="TutorCourse")

    def __str__(self):
        return self.user.first_name+' '+self.user.last_name

class StudentCourse(models.Model):
    course = models.ForeignKey(Course,related_name="course_name_student",on_delete=models.CASCADE)
    student = models.ForeignKey(Student,related_name="student_name",on_delete=models.CASCADE)

    def __str__(self):
        return self.student.user.username+' '+self.course.name

    class Meta:
        unique_together = ('course','student')

class TutorCourse(models.Model):
    course = models.ForeignKey(Course,related_name="course_name_tutor",on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor,related_name="tutor_name",on_delete=models.CASCADE)

    def __str__(self):
        return self.tutor.user.username+' '+self.course.name

    class Meta:
        unique_together = ('course','tutor')
