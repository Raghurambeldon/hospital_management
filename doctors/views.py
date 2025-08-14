# doctor/views.py
from django.shortcuts import render,get_object_or_404
from .models import Doctor, Disease

def doctor_list(request):
    doctors = Doctor.objects.filter(is_active=True)
    diseases = Disease.objects.all()  # ✅ Fetch all diseases

    # Filter doctors by selected disease
    disease_id = request.GET.get('disease')
    if disease_id:
        doctors = doctors.filter(diseases__id=disease_id)

    context = {
        'doctors': doctors,
        'diseases': diseases,  # ✅ pass diseases to template
        'selected_disease': disease_id  # optional: for keeping selection
    }
    return render(request, 'doctors/doctor-list.html', context)

def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    context = {
        'doctor': doctor
    }
    return render(request, 'doctors/doctor_detail.html', context)