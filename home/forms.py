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
    # first_name = forms.CharField(max_length=30, label='First Name')
    # phone = PhoneNumberField(label="Enter phone")
    # is_guardian = PhoneNumberField(label="Enter phone")
    # childs_name = PhoneNumberField(label="Enter phone")
    # already_diagnosed = PhoneNumberField(label="Enter phone")
    # booking_type = forms.ChoiceField(choices=BOOKING_TYPE, label="Classroom or Virtual")
    # booking_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}), label = "Date ")
    # time_slot = forms.ChoiceField(choices=TIME_SLOTS, label="Time")
    # class Meta:
    #     model = Booking
    #     fields = ('class_type', 'booking_type', 'booking_date',
    #               'time_slot',)
    
    class Meta:
        model = Client
        fields = ['phone']
    

class CustomPhoneNumberFormField(PhoneNumberField):
    pass
