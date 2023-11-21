
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users.views import login_user, logout_user, dashboard, applications, application_detail, save_application

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls')), 
    path('admission/', include('admission.urls')),
    
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
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