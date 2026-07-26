from django import forms
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = ['name', 'email', 'phone', 'qualification', 'skills', 'password']

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('password') != cleaned_data.get('confirm_password'):
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data