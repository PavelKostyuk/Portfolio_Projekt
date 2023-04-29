from django.contrib import admin
from .models import Project
# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title', 'description']
    list_filter = ['title']