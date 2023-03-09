from django.shortcuts import render

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
    return render(request, 'home.html', context)