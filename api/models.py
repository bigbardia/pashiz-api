from django.db import models

class Koochooloo(models.Model):

    name = models.CharField(max_length=100 , unique=True)
    pashiz = models.FloatField(default=0)

    def __str__(self):
        return f"{self.name} : {self.pashiz}"
