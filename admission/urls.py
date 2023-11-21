from django.urls import path
from . import views

urlpatterns = [
    path('new-application/', views.create_new_application, name="create-new-application"),
    path('application/<str:pk>/', views.get_application, name="application"),
    path('application/<str:pk>/saved/', views.application_saved, name="application-saved"),
    path('download-application/<str:pk>/', views.download_application, name="download-application"),
]
