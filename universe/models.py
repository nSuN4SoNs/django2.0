from typing import Type
from django.db import models
from django.db.models.fields import BooleanField
from django.urls import reverse

# Create your models here.


class Galaxy(models.Model):
    name = models.CharField(max_length=100)
    size_x = models.PositiveIntegerField()
    size_y = models.PositiveIntegerField()

    def __str__(self):
        return f"Name:{self.name} X:{self.size_x} Y:{self.size_y}"

    # class Meta:
    #     ordering = ["galaxy_star-system", "galaxy_star", "galaxy_planet"]


class StarSystem(models.Model):
    name = models.CharField(max_length=100)
    position_x = models.PositiveIntegerField()
    position_y = models.PositiveIntegerField()
    #galaxy = Foreign Key to Galaxy(fk)
    galaxy = models.ForeignKey(
        "star_system.Galaxy",
        on_delete=models.SET_NULL,
        null=True,
        related_name="star systems"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Star Systems"


class Star(models.Model):
    name = models.CharField(max_length=100)
    diameter = models.PositiveIntegerField()
    color = models.CharField(max_length=100)
    #star_system = Foreign Key to StarSystem(fk)
    star_system = models.ForeignKey(
        "star.StarSystem",
        on_delete=models.SET_NULL,
        null=True,
        related_name="stars"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Stars"


class Planet(models.Model):
    name = models.CharField(max_length=100)
    diameter = models.PositiveIntegerField()
    color = models.CharField(max_length=100)
    #star_system = Foreign Key to StarSystem(fk)
    star_system = models.ForeignKey(
        "planet.StarSystem",
        on_delete=models.SET_NULL,
        null=True,
        related_name="planets"
    )

    live = BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Planets"

