from rest_framework import serializers 
from .models import * 

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieListModel 
        fields = '__all__'