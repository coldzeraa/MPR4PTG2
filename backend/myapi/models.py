from django.db import models


class Point(models.Model):
    pID = models.AutoField(primary_key=True)     # ID
    x = models.IntegerField()                    # x coordinate
    y = models.IntegerField()                    # y coordinate
    quadrant = models.IntegerField()             # quadrant

    def __str__(self):
        return f"({self.x}|{self.y})"  # string representation as (x|y)



class Patient(models.Model):
    patID = models.AutoField(primary_key=True)
    lastName = models.CharField(max_length=50)       # last name
    firstName = models.CharField(max_length=50)      # first name

    def __str__(self):
        return f"{self.lastName} {self.firstName}"  # string representation as lastname firstname


class Examination(models.Model):
    exID = models.AutoField(primary_key=True)    # ID
    date = models.DateField()                       # date of examination

    patientID = models.ForeignKey(Patient, on_delete=models.CASCADE)   # patient


class PointResult(models.Model):
    resID = models.AutoField(primary_key=True)   # ID
    seen = models.BooleanField()                    # point seen (t/f)

    pointID = models.ForeignKey(Point, on_delete=models.CASCADE)              # point
    examinationID = models.ForeignKey(Examination, on_delete=models.CASCADE)  # examination
