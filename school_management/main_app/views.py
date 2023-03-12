from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from.models import *
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.


def is_student(user):
    return user.groups.filter(name='STUDENT').exists()


def is_teacher(user):
    return user.groups.filter(name='TEACHER').exists()


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
    student_list=Student.objects.filter(is_active=True)
    context['student_list']=student_list
    print(student_list,'---')
    return render(request, 'students.html', context)


def add_student(request):
    context={}
    class_list = Class.objects.all()
    context['class_list']=class_list
    if request.method == 'POST':
        name=request.POST['name']
        father_name=request.POST['father_name']
        phone=request.POST['phone']
        address=request.POST['address']
        class_id=request.POST['class_name']
        roll=request.POST['roll']
        is_active=request.POST.get('is_active')
        if is_active == '1':
            status=True
        else:
            status = False
        print(type(is_active),'---')
        class_instance = Class.objects.get(id=class_id)
        print(name, father_name, phone, address, class_id, is_active)
        Student.objects.create(name=name, father_name=father_name, phone=phone, address=address, class_name=class_instance, roll=roll, is_active=status)
    return render(request, 'add_student.html', context)


def edit_student(request, id):
    context={}
    class_list = Class.objects.all()
    context['class_list']=class_list
    student = Student.objects.get(id=id)
    context['student'] = student
    if request.method == 'POST':
        student_obj = get_object_or_404(Student, id=id)
        student_obj.name = request.POST['name']
        student_obj.father_name=request.POST['father_name']
        student_obj.phone=request.POST['phone']
        student_obj.address=request.POST['address']
        student_obj.roll=request.POST['roll']
        class_id=request.POST['class_name']
        is_active=request.POST.get('is_active')
        if is_active == '1':
            status=True
        else:
            status = False
        print(type(is_active),'---')
        class_instance = Class.objects.get(id=class_id)
        student_obj.class_name = class_instance
        student_obj.is_active = status
        student_obj.save()
        return redirect('students')
    return render(request, 'edit_student.html', context)


def delete_student(request, id):
    student_obj = Student.objects.get(id=id)
    student_obj.is_active=False
    student_obj.save()
    return redirect('students')



def class_subject(request):
    context={}
    context['subject_list']=Subject.objects.all()
    context['class_list']=Class.objects.all()
    if request.GET:
        class_id = int(request.GET.get('class_id'))
        subject_id = int(request.GET.get('subject_id'))
        class_obj = Class.objects.get(id=class_id)
        subject_obj = Subject.objects.get(id=subject_id)
        if subject_obj in class_obj.subjects.all():
            context['class_obj'] = class_obj
            context['subject_obj'] = subject_obj
            classwise_students=Student.objects.filter(class_name=class_obj)
            context['classwise_students'] = classwise_students




            # subject_obj = get_object_or_404(Subject, id=subject_id)
            # class_obj = get_object_or_404(Class, id=class_id)
            student_obj = get_object_or_404(Student, id=1)
            student_subjects=student_obj.class_name.subjects.all()
            class_ob = get_object_or_404(Class, id=class_id)
            for i in class_ob.subjects.all():
                if subject_obj == i:
                    class_ob.subjects.add(subject_obj)
                print(i.full_mark)




            # return HttpResponseRedirect(reverse('main_app:subject_marks_input', kwargs={'class_obj': class_obj, 'subject_obj':subject_obj}))
            return render(request, 'subject_marks_input.html', context)
        else:
            messages.error(request, "There is no subject on this class")
            return redirect('class-subject')

    return render(request, 'class_subject.html', context)


def subject_marks_input(request):
    context={}
    cls = Class.objects.get(name='Eight')
    print(cls,'---')
    # obj = Student.obejcts.get()
    return render(request, 'subject_marks_input.html', context)