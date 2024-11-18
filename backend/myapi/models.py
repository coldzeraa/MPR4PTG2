
from django.db import models


class Point(models.Model):

    pID = models.IntegerField(primary_key=True)  # ID
    x = models.IntegerField()                    # x coordinate
    y = models.IntegerField()                    # y coordinate
    quadrant = models.IntegerField()             # quadrant

    def __str__(self):
        return f"({self.x}|{self.y})"  # string representation as (x|y)


class Patient(models.Model):
    patID = models.AutoField(primary_key=True)
    lastName = models.CharField(max_length=50, null=True)       # last name
    firstName = models.CharField(max_length=50, null=True)      # first name
    email = models.EmailField(max_length=50, null=True)         # email
    password = models.CharField(max_length=100, null=True)      # password

    def __str__(self):
        return f"{self.lastName} {self.firstName} ({self.email})"  # string representation as lastname firstname (email)


class Examination(models.Model):
    TYPE_CHOICES =[('P', 'Perimetry'),
        ('I', 'Ishihara')]

    exID = models.AutoField(primary_key=True)  # ID
    date = models.DateTimeField()              # date and time of examination
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, default=None)  # type of examination
    pat = models.ForeignKey(Patient, on_delete=models.CASCADE)   # patient


class Result(models.Model):
    resID = models.AutoField(primary_key=True)   # ID
    ex = models.ForeignKey(Examination, on_delete=models.CASCADE) # examination
    
    class Meta:     # abstract result
        abstract = True


class ResultPerimetry(Result):
    p = models.ForeignKey(Point, on_delete=models.CASCADE)  # affected point
    seen = models.BooleanField()                            # boolean if point was seen
    

class ResultIshihara(Result):
    recognized = models.BooleanField()              # boolean if number was recognized
    filename = models.CharField(max_length=50)      # name of the file
    