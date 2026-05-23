from django.db import models
from patients.models import Patient
from doctors.models import Doctor


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Done', 'Done'),
        ('Cancelled', 'Cancelled'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor  = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date    = models.DateField()
    time    = models.TimeField()
    reason  = models.TextField()
    status  = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.name} -> Dr.{self.doctor.name} on {self.date}"

    class Meta:
        ordering = ['-date', '-time']
