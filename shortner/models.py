from django.db import models

# Create your models here.
class Link(models.Model):
    longLink = models.CharField(max_length=250)
    shortLink = models.CharField(max_length=250)

    def __str__(self) -> str:
        return super().__str__()