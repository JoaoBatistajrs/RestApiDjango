from django.db import models

class Register(models.Model):
  registerDay = models.DateField(null=True, blank=True)
  description = models.CharField(max_length=200)
  price = models.DecimalField(max_digits=9, decimal_places=2)
  category = models.CharField(max_length=50)

  def __str__(self):
    return self.description
