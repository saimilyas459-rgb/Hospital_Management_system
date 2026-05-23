from django.db import models

class Doctor(models.Model):
    SPECIALITIES = [
        ('General','General Physician'),
        ('Cardiology','Cardiology (Dil)'),
        ('Neurology','Neurology (Dimagh)'),
        ('Orthopedics','Orthopedics (Haddi)'),
        ('Pediatrics','Pediatrics (Bacha)'),
        ('Gynecology','Gynecology (Khawateen)'),
        ('Dermatology','Dermatology (Jild)'),
        ('ENT','ENT (Kaan Naak Gala)'),
        ('Ophthalmology','Ophthalmology (Aankh)'),
        ('Dentistry','Dentistry (Daant)'),
    ]

    name       = models.CharField(max_length=100)
    speciality = models.CharField(max_length=50, choices=SPECIALITIES)
    phone      = models.CharField(max_length=15)
    email      = models.EmailField(unique=True)
    fee        = models.DecimalField(max_digits=8, decimal_places=2)
    available  = models.BooleanField(default=True)
    joined     = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Dr. {self.name} - {self.speciality}"

    class Meta:
        ordering = ['name']
