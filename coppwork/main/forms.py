from django import forms
from .models import Worker, Company, Resume


class WorkerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['username', 'password', 'name', 'phone', 'email', 'age']
        widgets = {
            'password': forms.PasswordInput(),
            'phone': forms.TextInput(attrs={
                'data-mask': "+7(000)000-00-00",
                'placeholder': "+7(___)___-__-__",
                'type': "tel"
            }),
        }

class CompanyRegistrationForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['username', 'name', 'description', 'phone', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
            'description': forms.Textarea(),
            'phone': forms.TextInput(attrs={
                'data-mask': "+7(000)000 00 00",
                'placeholder': "+7(___)___ __ __",
                'type': "tel"
            }),
        }


class AddResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ["worker", "specializations", "salary", "work_experience", "type_employment", "work_schedule", "education", "file"]