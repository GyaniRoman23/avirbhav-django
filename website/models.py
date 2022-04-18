from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=30)

class Event(models.Model):
    name = models.CharField(max_length=30)
    winner = models.ForeignKey(Team, on_delete=models.CASCADE)
    
class Score(models.Model):
    value = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE) 
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

class Penalties(models.Model):
    value = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)