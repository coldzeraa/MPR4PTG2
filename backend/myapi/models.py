
from django.db import models


class Point(models.Model):

    pID = models.IntegerField(primary_key=True)     # ID
    x = models.IntegerField()                    # x coordinate
    y = models.IntegerField()                    # y coordinate
    quadrant = models.IntegerField()             # quadrant

    def __str__(self):
        return f"({self.x}|{self.y})"  # string representation as (x|y)


class Patient(models.Model):
    patID = models.AutoField(primary_key=True)
    lastName = models.CharField(max_length=50, null=True)       # last name
    firstName = models.CharField(max_length=50, null=True)      # first name
    email = models.EmailField(max_length=50, null=True)      # email
    password = models.CharField(max_length=100, null=True)        # password

    def __str__(self):
        return f"{self.lastName} {self.firstName} ({self.email})"  # string representation as lastname firstname (email)


class Examination(models.Model):
    exID = models.AutoField(primary_key=True)    # ID
    date = models.DateField()                       # date of examination
    type = models.CharField(max_length=1, default=None)       # Type of examination
    pat = models.ForeignKey(Patient, on_delete=models.CASCADE)   # patient


class Result(models.Model):
    resID = models.AutoField(primary_key=True)   # ID
    ex = models.ForeignKey(Examination, on_delete=models.CASCADE)             # Examination
    
    class Meta:                                     # Makes Result abstract
        abstract = True


class ResultPerimetry(Result):
    p = models.ForeignKey(Point, on_delete=models.CASCADE)  # Affected Point
    seen = models.BooleanField()                            # Boolean if point was seen
    

class ResultIshihara(Result):
    recognized = models.BooleanField()              # Boolean if image was recognized
    filename = models.CharField(max_length=50)      # Name of the file
    

