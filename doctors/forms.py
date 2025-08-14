from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'profile_image', 'specialization', 'diseases', 'rating', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'profile_image': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'specialization': forms.Select(attrs={'class':'form-control'}),
            'diseases': forms.SelectMultiple(attrs={'class':'form-control'}),
            'rating': forms.NumberInput(attrs={'class':'form-control', 'step':'0.1', 'min':'0', 'max':'5'}),
            'is_active': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }
