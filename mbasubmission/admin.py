from django.contrib import admin
from .models import Application

# Register your models here.
class ApplicationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Application, ApplicationAdmin)