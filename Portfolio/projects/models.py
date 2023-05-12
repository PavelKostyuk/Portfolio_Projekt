from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here
class Project(models.Model):
    title = models.CharField(max_length=250)
    description = RichTextUploadingField()
    project_image = models.ImageField(upload_to='media')
    


 
def __str__(self):
    return self.title