from django.db import models

# Create your models here.

class Parent(models.Model):
    pid = models.PositiveIntegerField(primary_key = True)
    name = models.CharField(max_length=80, null=False)
    # def __str__(self):
    #     return str(self.pid)
class Baby(models.Model):
    bid = models.PositiveIntegerField(primary_key = True)
    name = models.CharField(max_length = 80, null = False)
    pid = models.ForeignKey(
        'babyevents.Parent', 
        on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.name

class Event(models.Model):
    eid = models.PositiveIntegerField(primary_key = True)
    etype = models.CharField(max_length = 80, null = False)
    # time = models.DateField(auto_now = False, auto_now_add = True)
    comment = models.CharField(max_length=500)
    bid = models.ForeignKey(
        'babyevents.Baby',
        on_delete=models.CASCADE
    )
    # def __str__(self):
    #     return (self.etype + " " + self.comment)