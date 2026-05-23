from django.db import models
from patients.models import Patient


class Ward(models.Model):
    name     = models.CharField(max_length=50)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

    @property
    def occupied_count(self):
        return self.bed_set.filter(occupied=True).count()

    @property
    def free_count(self):
        return self.bed_set.filter(occupied=False).count()


class Bed(models.Model):
    ward     = models.ForeignKey(Ward, on_delete=models.CASCADE)
    bed_no   = models.CharField(max_length=10)
    patient  = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True, blank=True)
    occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"Bed {self.bed_no} - {self.ward.name}"

    class Meta:
        ordering = ['ward', 'bed_no']
