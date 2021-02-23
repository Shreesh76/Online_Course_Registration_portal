from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views 
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.Home,name='home'),

    path('login/',auth_views.LoginView.as_view(), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
 
    path('register/',views.register, name = 'register'),
    path('about/',views.about, name = 'about'),
    path('courses/',views.courses, name = 'courses'),
    path('courses/<int:pk>/',views.courses_list, name = 'courses_list'),



    path('activate/<uidb64>/<token>/',views.activate,name='activate'),

    path('profile/',views.profile, name = 'profile'),   


    path('your-courses/',views.uc, name = 'uc'),   
    path('done/',views.done, name = 'done'),   
    path('our-staff/',views.our_staff, name = 'teach'), 

    path('cart/<int:pk>',views.cart, name = 'cart'),  
    path('students_joined/<int:pk>',views.students_joined, name = 'students_joined'),  


    path('',RedirectView.as_view(url="home/")),
]
 