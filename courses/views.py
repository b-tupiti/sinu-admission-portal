from django.shortcuts import render
from .models import Course
from .utils import searchCourses, paginateCourses


def findcourse(request):
    
    courses, search = searchCourses(request)
    courses_total = courses.count()
    custom_range, courses, first_index, last_index = paginateCourses(request, courses, 5, courses_total)
    
    context = {
        'courses':courses,
        'courses_total': courses_total,
        'search':search,
        'custom_range': custom_range,
        'first_index': first_index,
        'last_index': last_index,
    }
    
    return render(request, 'courses/find-a-course.html', context)



def course(request, code):
    course = Course.objects.get(code=code)
    context = {'course':course}
    return render(request, 'courses/course-detail.html',context)


