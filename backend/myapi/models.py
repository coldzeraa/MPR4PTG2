from django.core.validators import RegexValidator
from django.db import models


class Point(models.Model):
    pID = models.IntegerField(primary_key=True)
    x = models.IntegerField()
    y = models.IntegerField()
    quadrant = models.IntegerField()

    def __str__(self):
        return f"({self.x}|{self.y})"


class Patient(models.Model):
    ssNr = models.IntegerField(primary_key=True, validators=[
        RegexValidator(r'^\d{10}$')])
    lastName = models.CharField()
    firstName = models.CharField()

    def __str__(self):
        return f"{self.lastName} {self.firstName}"


class Examination(models.Model):
    exID = models.IntegerField(primary_key=True)
    date = models.DateField()
    result = models.ManyToOneRel


class Result(models.Model):
    resID = models.IntegerField(primary_key=True)
    seen = models.BooleanField()





