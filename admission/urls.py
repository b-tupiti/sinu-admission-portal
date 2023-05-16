
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.submission_form, name="submission-form"), # old 
    # path('upload-my-deposit-slip/', views.upload_deposit_slip, name='upload-my-deposit-slip'), # old
    path('new-applicant/', views.create_new_admission, name="create-new-admission"),
    path('application/saved/', views.application_saved, name="application-saved"),
    path('application/<str:pk>/personal-details/', views.personal_details, name="personal-details"),
    path('application/<str:pk>/sponsor-details/', views.sponsor_details, name="sponsor-details"),
    path('application/<str:pk>/education-background/', views.education_background, name="education-background"),
    path('application/<str:pk>/employment-history/', views.employment_history, name="employment-history"),
    path('application/<str:pk>/declaration/', views.declaration, name="declaration"),
    path('my-admissions/', views.my_admissions, name="my-admissions"),
]
