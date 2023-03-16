
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.submission_form, name="submission-form"),
    path('upload_receipt/', views.upload_receipt, name='upload_receipt'),
]
