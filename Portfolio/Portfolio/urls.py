from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import projects
import projects.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', projects.views.home, name='home'),
    path('detail/<int:project_id>', projects.views.detail, name='detail')

] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)