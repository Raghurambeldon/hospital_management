from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time', 'disease', 'patient_name', 'dob', 'age', 'blood_group', 'address1', 'address2', 'nominee']
        widgets = {
            'date': forms.DateInput(attrs={'type':'date', 'class':'form-control'}),
            'time': forms.TimeInput(attrs={'type':'time', 'class':'form-control'}),
            'disease': forms.Select(attrs={'class':'form-control'}),
            'patient_name': forms.TextInput(attrs={'class':'form-control'}),
            'dob': forms.DateInput(attrs={'type':'date', 'class':'form-control'}),
            'age': forms.NumberInput(attrs={'class':'form-control'}),
            'blood_group': forms.Select(attrs={'class':'form-control'}),
            'address1': forms.TextInput(attrs={'class':'form-control'}),
            'address2': forms.TextInput(attrs={'class':'form-control'}),
            'nominee': forms.TextInput(attrs={'class':'form-control'}),
        }
