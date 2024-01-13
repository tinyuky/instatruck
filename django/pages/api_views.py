import pdb
from datetime import datetime

from django.db.models.expressions import Func, Value, F
from django.http.response import Http404
from rest_framework import generics, filters
from rest_framework.decorators import action
from rest_framework.fields import CharField
from rest_framework.response import Response

from .models import Movie, Actor, Director
from .serializers import MovieSerializer, ActorSerializer, DirectorSerializer
from .utls.custom_pagination import CustomPagination


class MovieViewSet(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['year']

    def get_queryset(self):
        queryset = Movie.objects.all()
        start_year = self.request.query_params.get('start_year', None)
        end_year = self.request.query_params.get('end_year', None)

        if start_year:
            queryset = queryset.filter(year__gte=start_year)
        if end_year:
            queryset = queryset.filter(year__lte=end_year)

        return queryset

class BestMovieViewSet(generics.ListAPIView):
    serializer_class = MovieSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['rating', 'metascore']

    @action(detail=False, methods=['get'])
    def get_queryset(self):
        queryset = Movie.objects.all()

        n = self.kwargs['n'] if 'n' in self.kwargs else None
        queryset = queryset.order_by('-rating', '-metascore')

        if n:
            queryset = queryset[:n]

        return queryset

class ActorViewSet(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    pagination_class = CustomPagination

class ActorFilmsViewSet(generics.ListAPIView):
    serializer_class = MovieSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        actor_name = self.kwargs['name']
        return Movie.objects.filter(actor__name=actor_name)

class ClosestBirthdaysActorViewSet(generics.ListAPIView):
    serializer_class = ActorSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['birthdate']
    pagination_class = CustomPagination

    def get_queryset(self):
        date_str = self.kwargs.get('date', None)

        if not date_str:
            raise Http404("Date parameter is required")

        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            raise Http404("Invalid date format. Use 'DDMMYYYY'")

        queryset = Actor.objects.all()

        queryset = sorted(queryset,
                          key=lambda actor: abs((datetime.strptime(actor.date, '%Y-%m-%d').date() - date).days))

        return queryset

class DirectorViewSet(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    pagination_class = CustomPagination

class DirectorFilmsViewSet(generics.ListAPIView):
    serializer_class = MovieSerializer
    pagination_class = CustomPagination
    def get_queryset(self):
        director_name = self.kwargs['name']
        return Movie.objects.filter(director__name=director_name)
