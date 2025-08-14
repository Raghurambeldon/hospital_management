from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .forms import AppointmentForm
from .models import Appointment
from doctors.models import Doctor
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from xhtml2pdf import pisa
import random

@login_required
def book_appointment(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.doctor = doctor
            appointment.user = request.user
            appointment.token_number = f"TOKEN-{random.randint(1000,9999)}"
            appointment.save()
            return redirect('appointment_success', appointment_id=appointment.id)
    else:
        form = AppointmentForm()

    return render(request, 'appointments/bookanappointment.html', {
        'form': form,
        'doctor': doctor
    })


@login_required
def appointment_success(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)

    template_path = 'appointments/appointment_pdf.html'
    context = {'appointment': appointment}

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="Appointment_{appointment.token_number}.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors while generating PDF <pre>' + html + '</pre>')
    return response
