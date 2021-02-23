from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/',views.contact_view,name='contact_view'),
] 


