from django.shortcuts import render
from .models import course , category , trainers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def courses(request):
    courses = course.objects.all()
    context = {
        'cr' : courses
    }
    return render(request , 'courses/courses.html', context=context)



