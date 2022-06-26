from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=50)
    age = models.FloatField()
    weight = models.FloatField()
    sex = models.CharField(max_length=15)
    group = models.ForeignKey("groups.Group", on_delete=models.SET_NULL, blank=True, null=True)
   
    def __repr__(self):
        return f"Animal {self.id} - {self.name} "