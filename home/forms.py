from django import forms
from .models import Client

class ClientDetailsForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'phone', 'is_guardian', 'childs_name',
                  'already_diagnosed',)
    