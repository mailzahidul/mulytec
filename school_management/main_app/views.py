from django.shortcuts import render
from.models import *
# Create your views here.

def home(request):
    context={}
    dic=['male','female']
    dic1=[20,30]
    context['gender_list']=dic
    context['gender_number']=dic1

    course_list=['Computer Science','Machanical Engineering','Electrical Engineering','Architecture']
    number_list=[20,30,40,50]
    context['course_list']=course_list
    context['number_list']=number_list

    students=Student.objects.all().count()
    context['total_students']=students

    return render(request, 'home.html', context)



def students(request):
    context={}
    student_list=Student.objects.all()
    context['student_list']=student_list
    print(student_list,'---')
    return render(request, 'students.html', context)