from django.db import models

# Predefined specializations
SPECIALIZATION_CHOICES = [
    ('Cardiology', 'Cardiology'),
    ('Dermatology', 'Dermatology'),
    ('Pediatrics', 'Pediatrics'),
    ('Neurology', 'Neurology'),
    ('Orthopedics', 'Orthopedics'),
    ('General', 'General'),
]

# Predefined diseases
DISEASE_CHOICES = [
    ('Cold', 'Cold'),
    ('Cough', 'Cough'),
    ('Fever', 'Fever'),
    ('Back Pain', 'Back Pain'),
    ('Neck Pain', 'Neck Pain'),
    ('Headache', 'Headache'),
    ('Acne', 'Acne'),
    ('Skin Rash', 'Skin Rash'),
    ('Child Fever', 'Child Fever'),
    ('Fracture', 'Fracture'),
]

class Disease(models.Model):
    name = models.CharField(max_length=100, choices=DISEASE_CHOICES, unique=True)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    profile_image = models.ImageField(
        upload_to='images/doctors/',  # will store in MEDIA_ROOT/images/doctors/
        default='images/doctors/default.png',
        blank=True
    )
    specialization = models.CharField(max_length=50, choices=SPECIALIZATION_CHOICES)
    diseases = models.ManyToManyField(Disease, related_name='doctors')
    rating = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.specialization})"
