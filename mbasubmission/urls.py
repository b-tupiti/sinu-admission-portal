
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.submission_form, name="submission-form"),
    path('upload-my-deposit-slip/', views.upload_deposit_slip, name='upload-my-deposit-slip'),
]
