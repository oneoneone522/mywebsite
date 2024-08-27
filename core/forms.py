from django import forms
from .models import ClientInfo

class QuotationForm(forms.ModelForm):
    class Meta:
        model = ClientInfo
        fields = ['contact_choice', 'name', 'phone_num', 'Line_ID', 'email_add', 'industry', 'web_type']
