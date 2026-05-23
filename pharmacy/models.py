from django.db import models


class Medicine(models.Model):
    name    = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    price   = models.DecimalField(max_digits=8, decimal_places=2)
    stock   = models.IntegerField(default=0)
    expiry  = models.DateField()
    added   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def is_low_stock(self):
        return self.stock <= 10

    class Meta:
        ordering = ['name']
