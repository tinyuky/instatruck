from rest_framework import serializers
from .models import Movie, Actor, Director

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'description', 'rating', 'director']

class ActorSerializer(serializers.ModelSerializer):
    birthdate = serializers.SerializerMethodField()
    birthplace = serializers.SerializerMethodField()
    films = serializers.HyperlinkedIdentityField(view_name='actor-films-api', lookup_field='name')

    class Meta:
        model = Actor
        fields = ['name', 'birthdate', 'birthplace', 'films']

    def get_birthdate(self, obj):
        return str(obj.date)

    def get_birthplace(self, obj):
        return str(obj.place)

    def get_films_url(self, obj):
        # Assuming 'actor-films' is the name of the view for actor films
        return f'/actors/{obj.name}/films/'

class DirectorSerializer(serializers.ModelSerializer):
    birthdate = serializers.SerializerMethodField()
    birthplace = serializers.SerializerMethodField()
    films = serializers.HyperlinkedIdentityField(view_name='director-films-api', lookup_field='name')
    class Meta:
        model = Director
        fields = ['name', 'birthdate', 'birthplace', 'films']

    def get_birthdate(self, obj):
        return str(obj.date)

    def get_birthplace(self, obj):
        return str(obj.place)

    def get_films_url(self, obj):
        # Assuming 'actor-films' is the name of the view for actor films
        return f'/directors/{obj.name}/films/'
