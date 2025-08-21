from django import forms
from django.contrib.auth.models import User
from .models import Booking

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def clean(self):
        cleaned = super().clean()
        if cleaned.get('password') != cleaned.get('confirm_password'):
            raise forms.ValidationError('Passwords do not match')
        return cleaned

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['seats']
        widgets = {
            'seats': forms.NumberInput(attrs={'min': 1})
        }

    def __init__(self, *args, **kwargs):
        self.travel_option = kwargs.pop('travel_option')
        super().__init__(*args, **kwargs)

    def clean_seats(self):
        seats = self.cleaned_data['seats']
        if seats < 1:
            raise forms.ValidationError('You must book at least 1 seat')
        return seats
