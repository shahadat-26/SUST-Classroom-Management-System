from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Building(models.Model):

    name = models.CharField(max_length=200,null=False)

class Classroom(models.Model):

    room_no = models.CharField(max_length=200,null=False)
    room_type = models.CharField(max_length=200, null=False)
    capacity = models.IntegerField(null=False,blank=False)
    room_status = models.BooleanField(default=False)
    building = models.ForeignKey(Building, on_delete=models.CASCADE,null=True,blank=False)

class ClassTime(models.Model):

    date = models.DateField()
    classroom = models.ForeignKey(Classroom,on_delete=models.CASCADE,null=False,blank=False)
    shift1 = models.BooleanField(default=False)
    shift2 = models.BooleanField(default=False)
    shift3 = models.BooleanField(default=False)
    shift4 = models.BooleanField(default=False)
    shift5 = models.BooleanField(default=False)
    shift6 = models.BooleanField(default=False)
    shift7 = models.BooleanField(default=False)
    shift8 = models.BooleanField(default=False)
    shift9 = models.BooleanField(default=False)
    shift10 = models.BooleanField(default=False)
    shift11 = models.BooleanField(default=False)
    shift12 = models.BooleanField(default=False)

class Track(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False)
    classroom = models.ForeignKey(Classroom,on_delete=models.CASCADE,null=False,blank=False)
    time = models.IntegerField(null=False,blank=False)
    date = models.DateField()

