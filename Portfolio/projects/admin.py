from django.contrib import admin
from django.db import models
from ckeditor.widgets import CKEditorWidget
from .models import Project
from django import forms

class ProjectAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Project
        fields = '__all__'

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title', 'description']
    list_filter = ['title']
    form = ProjectAdminForm

    # Override the formfield for the description field to use CKEditor
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }