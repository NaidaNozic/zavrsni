from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from courses.forms import NewUserForm, StudentProfileForm, QuestionForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Course,Notice,Question,Student
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

# Create your views here.

def user_login(request):
   if request.method == "POST":
      username = request.POST['usernameInput']
      password = request.POST['passwordInput']
      user = authenticate(request,username=username,password=password)

      if user is not None:
         login(request,user)
         return redirect('dashboard')

      else:
         messages.error(request, "Invalid Details")
         return redirect('login')
   else:
      return render(request,'authenticate/login.html',{})

def user_logout(request):
   logout(request)
   messages.success(request,"Your were logged out!")
   return redirect("home")

def register_student(request):
   if request.method=="POST":
      user_form = NewUserForm(data = request.POST)
      student_form = StudentProfileForm(data = request.POST)

      if user_form.is_valid() and student_form.is_valid():

         user = user_form.save()
         user.is_student = True
         user.save()
         student = student_form.save(commit=False)
         student.user=user
         student.save()
         login(request, user)
         messages.success(request,"Registration successful!")
         return redirect('dashboard')

      else:
         print(user_form.errors,student_form.errors)
   else:
      user_form = NewUserForm()
      student_form = StudentProfileForm()

   return render(request,'authenticate/register_student.html',{'user_form':user_form,'student_form':student_form})

def dashboard(request):
   courses = Course.objects.all()
   return render(request,"courses/all_courses.html",{'all_courses':courses})

def view_course(request,course_id):
   course = get_object_or_404(Course,pk=course_id)
   notices = Notice.objects.filter(course=course)
   questions = Question.objects.filter(course=course)

   if request.method=="POST":
      question_form = QuestionForm(data = request.POST)

      if question_form.is_valid():

         question = question_form.save(commit=False)
         question.course = course
         question.student = get_object_or_404(Student,pk=request.user.id)
         question.save()
         #return HttpResponseRedirect(request.path_info)
         return render(request,"courses/course.html",{'course':course,'notices':notices,'questions':questions,'question_form':question_form})

      else:
         print(question_form.errors)

   else:
      question_form = QuestionForm()

   return render(request,"courses/course.html",{'course':course,'notices':notices,'questions':questions,'question_form':question_form})