from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):

    user = models.OneToOneField(User)
    enrol = models.IntegerField()

    def __str__(self):
        return self.user.email


class Attendance(models.Model):

    enrol = models.IntegerField()
    present = models.BooleanField(default=False)
    add_date = models.DateTimeField()


class SubjectWiseAttendance(models.Model):

    subject1 = models.IntegerField(default=0)
    subject2 = models.IntegerField(default=0)
    subject3 = models.IntegerField(default=0)
    subject4 = models.IntegerField(default=0)
    subject5 = models.IntegerField(default=0)

    enrol = models.IntegerField()


class Result(models.Model):

    marksInSubject1 = models.IntegerField(default=0)
    marksInSubject2 = models.IntegerField(default=0)
    marksInSubject3 = models.IntegerField(default=0)
    marksInSubject4 = models.IntegerField(default=0)
    marksInSubject5 = models.IntegerField(default=0)

    enrol = models.IntegerField()