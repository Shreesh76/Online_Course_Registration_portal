from django.shortcuts import render, redirect
from contact.forms import ContactForm
from contact.models import contact


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            department = form.cleaned_data['department']
            roll_no = form.cleaned_data['roll_no']
            message = form.cleaned_data['message']

            contact.objects.create(name=name,email=email,department=department,roll_no=roll_no,message=message)
            
            return redirect('contact_view')
    return render(request,'contact.html')