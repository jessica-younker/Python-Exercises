from django.db import models

# Build a model representing your Artist table.
# Build a model representing your Song table. Ensure 
# that you define the foreign key to the artist table.
class Song(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=100)
    song = models.ForeignKey(Song)

    def __str__(self):
        return self.name