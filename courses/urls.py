from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_courses, name="search-courses"),
    path('course-detail/<str:code>/', views.course, name="course-detail"),
  
]