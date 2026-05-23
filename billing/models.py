from django.db import models
from patients.models import Patient


class Bill(models.Model):
    patient     = models.ForeignKey(Patient, on_delete=models.CASCADE)
    amount      = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    paid        = models.BooleanField(default=False)
    date        = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bill #{self.id} - {self.patient.name} - Rs.{self.amount}"

    class Meta:
        ordering = ['-date']
