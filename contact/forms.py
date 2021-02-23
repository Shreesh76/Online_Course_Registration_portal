from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(required=False) 
    roll_no = forms.CharField(required=False)
    department = forms.CharField(required=False)
    message = forms.CharField(required=False)