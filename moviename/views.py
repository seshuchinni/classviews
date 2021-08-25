from django.shortcuts import render
from .models import * 
from .serializers import *
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

class MoviesLists(ListAPIView):
    queryset = MovieListModel.objects.all()
    serializer_class = MovieSerializer

class MoviesListsCreate(CreateAPIView):
    queryset = MovieListModel.objects.all()
    serializer_class = MovieSerializer

class MoviesListsRetrive(RetrieveAPIView):
    queryset = MovieListModel.objects.all()
    serializer_class = MovieSerializer

class MoviesListsUpdate(UpdateAPIView):
    queryset = MovieListModel.objects.all()
    serializer_class = MovieSerializer


class MoviesListsDelete(DestroyAPIView):
    queryset = MovieListModel.objects.all()
    serializer_class = MovieSerializer
