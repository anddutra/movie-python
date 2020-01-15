from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    title = models.CharField(max_length=100)

class ActorMovie(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.PROTECT, related_name='actor_fk', null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='actorsmovie')

    @property
    def getActorName(self):
        return self.actor.name

    @property
    def getMovieTitle(self):
        return self.movie.title