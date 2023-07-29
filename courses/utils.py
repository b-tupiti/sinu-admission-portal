from .models.course import Course
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def course_does_not_exist(code):
    """
    checks if course does not exist based on code argument. Helpful in cases where you want
    to redirect a user if this resolves to True.
    """
    return not Course.objects.filter(code=code).exists()


def filter_courses(request):
    
    search = ''
    
    if request.GET.get('search'):
        search = request.GET.get('search')
    
    courses = Course.objects.distinct().filter(
        Q(title__icontains=search) |
        Q(code__icontains=search)
    )
    
    return courses, search


def paginate_courses(request, courses, results, courses_total):

    page = request.GET.get('page')
    paginator = Paginator(courses, results)
    
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        courses = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        courses = paginator.page(page)
    
    
    leftIndex = (int(page) - 4)
       
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)
    
    first_index = (int(page) - 1) * results + 1
    last_index = first_index + results - 1
    
    if last_index > courses_total:
        last_index = courses_total
    
    return custom_range, courses, first_index, last_index