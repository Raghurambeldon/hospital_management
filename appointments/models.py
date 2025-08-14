from django.db import models
from django.contrib.auth.models import User
from doctors.models import Doctor
from doctors.models import Disease

BLOOD_GROUP_CHOICES = [
    ('A+', 'A+'), ('A-', 'A-'),
    ('B+', 'B+'), ('B-', 'B-'),
    ('O+', 'O+'), ('O-', 'O-'),
    ('AB+', 'AB+'), ('AB-', 'AB-'),
]

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    disease = models.ForeignKey(Disease, on_delete=models.SET_NULL, null=True)
    patient_name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, blank=True)
    nominee = models.CharField(max_length=100, blank=True)
    token_number = models.CharField(max_length=20, blank=True)  # optional

    def __str__(self):
        return f"{self.patient_name} - {self.doctor.name} on {self.date} at {self.time}"
