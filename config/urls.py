
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users.views import LoginUser, LogoutUser, Dashboard, Applications, ApplicationDetail, SaveId

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('mba-admission/', include('admission.urls')),
    path('', include('courses.urls')), # path: find-a-course 
    path('admission/', include('admission.urls')),
    
    path('login/', LoginUser, name='login'),
    path('logout/', LogoutUser, name='logout'),
    path('dashboard/', Dashboard, name='dashboard'),
    path('dashboard/applications/', Applications, name='applications'),
    path('dashboard/applications/<str:filter>/', Applications, name='applications'),
    path('dashboard/application/<str:pk>/', ApplicationDetail, name='application-detail'),
    path('dashboard/application/<str:pk>/save-id/', SaveId, name='save-id'),
]

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)