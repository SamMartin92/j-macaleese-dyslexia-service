from django import forms
from .models import Client
from allauth.account.forms import SignupForm
from phonenumber_field.formfields import PhoneNumberField


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    
 
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class ClientDetailsForm(forms.ModelForm):
    
    class Meta:
        model = Client
        fields = ['phone']
    

