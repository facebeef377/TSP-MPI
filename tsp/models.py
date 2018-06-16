from django.db import models
from django.utils import timezone
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    owner_id=models.IntegerField()
    instance_id=models.IntegerField()
    population=models.IntegerField()
    generations=models.IntegerField()
    wpz=models.IntegerField()
    proc=models.IntegerField()
    
    def add(self):
        self.save()

    def __str__(self):
        return self.title

    def getstatus(self):
        return self.status

    def setstatus(self,stat):
        self.status = stat

class Instance(models.Model):
    owner_id=models.IntegerField()
    graph=models.TextField(max_length=40000)
    cityCount=models.IntegerField()
    title=models.CharField(max_length=200)

    def add(self):
        self.save()

    def __str__(self):
        return self.title

class History(models.Model):
    owner_id=models.IntegerField()
    title = models.CharField(max_length=200)
    cityCount=models.IntegerField()
    graph=models.TextField(max_length=40000)
    time = models.CharField(max_length=200)
    population=models.IntegerField()
    generations=models.IntegerField()
    wpz=models.IntegerField()
    proc=models.IntegerField()
    
    def add(self):
        self.save()

    def __str__(self):
        return self.title