from django.db import models


class Characteristic(models.Model):
    name = models.CharField(max_length=20, unique=True)
    animals = models.ManyToManyField("animals.Animal", related_name="characteristics")
    #animal = models.ForeignKey("animals.Animal", on_delete=models.CASCADE, related_name="characteristics")

