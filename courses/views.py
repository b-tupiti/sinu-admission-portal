from django.shortcuts import render
from .models.course import Course
from .models.courseunit import CourseUnit
from .utils import filter_courses, paginate_courses


def findcourse(request):
    
    courses, search = filter_courses(request)
    courses_total = courses.count()
    custom_range, courses, first_index, last_index = paginate_courses(request, courses, 5, courses_total)
    
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
    core_units = CourseUnit.objects.filter(course=course,unit_type='core')
    electives = CourseUnit.objects.filter(course=course,unit_type='elective')
    context = {'course':course,'core_units':core_units,'electives':electives}
    return render(request, 'courses/course-detail.html',context)


