from django import forms
from .models import Ticket

class TicketForm(forms.Form):
    name = forms.CharField(max_length=250, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    subject = forms.CharField(max_length=250, required=True)
    phone = forms.CharField(max_length=11, required=True)