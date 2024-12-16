from django import forms
from .models import Ticket


class TicketForm(forms.Form):
    subject_choice = (
        ("پیشنهاد دادن" , "پیشنهاد دادن"),
        ("انتقاد", "انتقاد"),
        ("گزارش مشکل" , "گزارش مشکل"),
    )

    name = forms.CharField(max_length=250, required=True, label='نام')
    email = forms.EmailField(required=True, label='ایمیل')
    message = forms.CharField(widget=forms.Textarea, required=True, label='پیام شما')
    subject = forms.ChoiceField(choices=subject_choice, required=True, label='موضوع')
    phone = forms.CharField(max_length=11, required=True, label='شماره تلفن')

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not phone.isdigit():
            raise forms.ValidationError('شماره تلفن باید عدد باشد')
        return phone

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("به پایان برسد @gmail.com ایمیل حتما باید با")
        return email

    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message) < 10:
            raise forms.ValidationError('پیام شما باید حداقل 10 کاراکتر باشد')
        return message
