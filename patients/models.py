from django.db import models

class Patient(models.Model):
    BLOOD_GROUPS = [
        ('A+','A+'), ('A-','A-'), ('B+','B+'), ('B-','B-'),
        ('O+','O+'), ('O-','O-'), ('AB+','AB+'), ('AB-','AB-'),
    ]
    GENDER_CHOICES = [('Male','Male'), ('Female','Female'), ('Other','Other')]

    name        = models.CharField(max_length=100)
    age         = models.IntegerField()
    gender      = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone       = models.CharField(max_length=15)
    address     = models.TextField()
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUPS)
    registered  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-registered']
