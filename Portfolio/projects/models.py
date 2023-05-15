from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django import forms    
from ckeditor_uploader.widgets import CKEditorUploadingWidget


# Create your models here
class Project(models.Model):
    title = models.CharField(max_length=250)
    description = RichTextUploadingField()
    project_image = models.ImageField(upload_to='media')


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'project_image']
        widgets = {
            'description': CKEditorUploadingWidget(),
        }
    

def __str__(self):
    return self.title