from django.urls import path
from . import views

urlpatterns = [
    path('', views.findcourse, name="find-course"),
    path('course-detail/<str:code>/', views.course, name="course-detail"),
  
]