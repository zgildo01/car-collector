from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator

class Mod(models.Model):
  name = models.CharField(max_length=50)
  price=models.FloatField(
    validators=[MinValueValidator(0.0)]
  )

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      return reverse("mods_detail", kwargs={"pk": self.id})

class Car(models.Model):
  make = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  year = models.IntegerField()
  quote = models.TextField(max_length=250)
  mods = models.ManyToManyField(Mod)

  def __str__(self):
    return self.model
  
  def get_absolute_url(self):
    return reverse('cars_detail', kwargs={'car_id': self.id})

class Servicing(models.Model):
  date = models.DateField('Servicing Date')
  work_done = models.TextField(max_length=250)
  car = models.ForeignKey(Car, on_delete=models.CASCADE)
  def __str__(self):
    return f"Servicing: {self.work_done} on {self.date}"
  class Meta:
    ordering = ['-date']

  