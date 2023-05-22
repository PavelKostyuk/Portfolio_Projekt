from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
import pytz
from django.utils import timezone
from datetime import datetime


def default_created_at():
    tz = pytz.timezone('Europe/Stockholm')
    return timezone.make_aware(datetime.now(), tz)

def default_updated_at():
    return timezone.now()


class Project(models.Model):
    title = models.CharField(max_length=250)
    description = RichTextUploadingField()
    project_image = models.ImageField(upload_to='media')
    created_at = models.DateTimeField(default=default_created_at)
    updated_at = models.DateTimeField(default=default_updated_at)

    def __str__(self):
        return self.title

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'project_image', 'created_at', 'updated_at']
        widgets = {
            'description': CKEditorUploadingWidget(),
        }