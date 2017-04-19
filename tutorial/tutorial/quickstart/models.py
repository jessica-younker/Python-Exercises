from django.db import models

# Create your models here.
class HockeyTeam(models.Model):
    teamname = models.CharField(max_length=44)
    logo = models.FilePathField()
    city = models.CharField(max_length=255)
    coach = models.CharField(max_length=55)
    mascot = models.CharField(max_length= 60)

    def __str__(self):
        return self.teamname

class HockeyPlayer(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(HockeyTeam, related_name='players')
    position = models.CharField(max_length=50)
    

class CatBreed(models.Model):
    name = models.CharField(max_length=44)
    temperment = models.CharField(max_length=44)
    hair_length = models.CharField(max_length=44)
    