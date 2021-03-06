from typing import Type
from django.db import models
from django.urls import reverse

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)
    vin_number = models.CharField(max_length=100)
    car_model = models.ForeignKey(
        "car.CarModel",
        on_delete=models.SET_NULL,
        null=True,
        related_name="cars"
    )
    car_colour = models.ForeignKey(
        "car.Colour",
        on_delete=models.SET_NULL,
        null=True,
        related_name="cars"
    )
    car_rlsdate = models.ForeignKey(
        "car.Rlsdate",
        on_delete=models.SET_NULL,
        null=True,
        related_name="cars"
    )
    car_kind = models.ForeignKey(
        "car.Kind",
        on_delete=models.SET_NULL,
        null=True,
        related_name="cars"
    )

    def company(self):
        if self.car_model:
            return self.car_model.company
        return None

    def colour(self):
        if self.car_model:
            return self.car_model.colour
        return None

    def rlsdate(self):
        if self.car_model:
            return self.car_model.rlsdate
        return None

    def kind(self):
        if self.car_model:
            return self.car_model.kind
        return None

    def __str__(self):
        return f"Name:{self.name} vin_number: {self.vin_number}"

    def get_absolute_url(self):
        return reverse('car-detail', kwargs={'pk' : self.pk})

    class Meta:
        ordering = ["car_model", "car_colour", "car_rlsdate", "car_kind"]

class CarModel(models.Model):

    name = models.CharField(max_length=100)
    company = models.ForeignKey("car.Company", on_delete=models.SET_NULL, null=True)
    colour = models.ForeignKey("car.Colour", on_delete=models.SET_NULL, null=True)
    rlsdate = models.ForeignKey("car.Rlsdate", on_delete=models.SET_NULL, null=True)
    kind = models.ForeignKey("car.Kind", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Company(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"

class Colour(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Colours"

class Rlsdate(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Release dates"

class Kind(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Kinds"

