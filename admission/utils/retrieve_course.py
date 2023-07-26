from courses.models.course import Course

def get_course_from_code(request):
    course_code = request.GET.get('course_code')
    course =  Course.objects.values('code', 'title', 'campus').get(code=course_code)
    return course