from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    release_year = models.IntegerField()
    rating = models.FloatField(null=True, blank=True)
    cover = models.ImageField(upload_to='movie/covers/', null=True, blank=True)

    def __str__(self):
        return self.title


class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class MovieActor(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
