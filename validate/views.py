from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from validate.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Profile

from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.shortcuts import HttpResponse, HttpResponseRedirect

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage

from validate.models import Courses,teachers

def Home(request):
    return render(request, 'index2.html')



def courses(request):
    obj = Courses.objects.all() # SELECT * FROM Courses
    context = {
        'obj':obj,
    }
    return render(request, 'course-grid.html',context)


def courses_list(request, *args, **kwargs):
    obj = get_object_or_404(Courses, pk=kwargs.get("pk")) # SELECT * FROM Courses where id = pk
    context = {
        'obj' : obj,
    }
    return render(request, 'course-single.html',context)


def about(request):
    return render(request, 'page-about.html')



def done(request, *args, **kwargs):
    post = get_object_or_404(Courses, pk=request.POST.get("post_id")) # SELECT * FROM Courses where id = pk
    a = Profile.objects.get(user=request.user)   # SELECT * from Profile where user = current.user
    post.students.add(a)        
    return render(request, 'done.html')

def uc(request):
    obj1 = Profile.objects.get(user=request.user)
    obj = Courses.objects.all()
    context = {
        'obj1':obj1,
        'obj':obj,
    }
    return render(request, 'uc.html',context)

def cart(request, *args, **kwargs):
    obj = get_object_or_404(Courses, pk=kwargs.get("pk"))  
    context = {
        'obj' : obj,
    }
    return render(request, 'page-shop-cart.html',context)

def students_joined(request, *args, **kwargs):
    obj1 = get_object_or_404(Courses, pk=kwargs.get("pk"))  # SELECT * FROM Courses where id = pk
    obj = obj1.students.all() 
    context = {
        'obj' : obj,
    }
    return render(request, 'students.html',context)

def our_staff(request):
    obj = teachers.objects.all()
    context = {
        'obj':obj,
    }
    return render(request, 'course-instructors.html',context)



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            # username = form.cleaned_data.get('username')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')         
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            if Profile.objects.filter(user=request.user) or request.user.is_superuser:
                Profile.objects.update(
                                         Name=p_form.cleaned_data['Name'],
                                         Roll_No=p_form.cleaned_data['Roll_No'],
                                         Year=p_form.cleaned_data['Year'],
                                         department=p_form.cleaned_data['department'],
                                         )
            else:
                Profile.objects.create(user=request.user,
                                         Name=p_form.cleaned_data['Name'],
                                         Roll_No=p_form.cleaned_data['Roll_No'],
                                         Year=p_form.cleaned_data['Year'],
                                         department=p_form.cleaned_data['department'],
                                         )

            # contact_email = request.user.email
            # send_mail(
            #     'Updated the Profile',
            #     'Your profile has been successfully updated',
            #     'app.info.45@gmail.com',
            #     [contact_email],
            # )
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)

def activate(request, uidb64, token):   
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, f'Your account has been created! You are now able to log in')
        return redirect('login')
    else:
        return HttpResponse('Activation link is invalid!')

