from django.db import models
from django.db.models import ForeignKey


class Country(models.Model):
    # categorii
    id = models.AutoField(primary_key=True)
    name = models.CharField("Country", max_length=150)
    description = models.TextField("desc")

    def __str__(self):
        return self.name

    
    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Country"

class Work(models.Model):

    name = models.CharField("Work",max_length=150)
    description = models.TextField("desc")
    salary = models.CharField("salary",max_length=150)
    country = models.ForeignKey(Country, verbose_name = "Country", on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name

    
    class Meta:
        verbose_name = "Work"
        verbose_name_plural = "Work"
