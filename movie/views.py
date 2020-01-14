from django.shortcuts import render
from rest_framework import viewsets
from .models import Actor, Movie
from .serializer import ActorSerializer, MovieSerializer
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.
class ActorAPI(viewsets.ModelViewSet):
    queryset = Actor.objects.all().order_by('id')
    serializer_class = ActorSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['name']

class MovieAPI(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('id')
    serializer_class = MovieSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'actorsmovie__actor__name')