from django.shortcuts import render
from .models import Course

def findcourse(request):
    
    search = ''
    if 'search' in request.GET:
        search = request.GET['search']
        courses = Course.objects.filter(title__contains=search)
        context = {
            'search': search,
            'courses': courses,
        }
    else:
        context = {
            'search': search
        }
    
    return render(request, 'courses/find-a-course.html', context)




def course(request, code):
    course = Course.objects.get(code=code)
    context = {'course':course}
    return render(request, 'courses/course-detail.html',context)


