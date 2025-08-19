from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.charField(max_length=200)

    def __str__(self):
        return self.name