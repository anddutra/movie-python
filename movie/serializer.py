from rest_framework import serializers
from .models import Actor, Movie, ActorMovie

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class ActorMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActorMovie
        fields = ('id', 'actor')

class MovieSerializer(serializers.ModelSerializer):
    actorsmovie = ActorMovieSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def create(self, validated_data):
        actorsmovie_data = validated_data.pop('actorsmovie')
        movie = Movie.objects.create(**validated_data)
        for actor_data in actorsmovie_data:
            ActorMovie.objects.create(
                movie=movie, **actor_data)
        return movie