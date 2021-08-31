from django.shortcuts import render
from .models import * 
from .serializers import *
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
#from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser



class MoviesLists(ListAPIView):
    queryset = MovieListModel.objects.all()
    serializer_class = MovieSerializer
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]

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
   
   