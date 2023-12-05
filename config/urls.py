
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users.views import (
    login_user, 
    logout_user, 
    dashboard, 
    applications, 
    application_detail, 
    save_application
)
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls')), 
    path('admission/', include('admission.urls')),
    
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='users/reset_password.html', html_email_template_name='users/reset_password_email_template.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='users/reset_password_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/reset_password_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/reset_password_complete.html'), name='password_reset_complete'),
    
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/applications/', applications, name='applications'),
    path('dashboard/applications/<str:filter>/', applications, name='applications'),
    path('dashboard/application/<str:pk>/', application_detail, name='application-detail'),
    path('dashboard/application/<str:pk>/save-id/', save_application, name='save-id'),
]

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)