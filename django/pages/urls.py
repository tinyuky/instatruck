from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

from . import views
from .api_views import MovieViewSet, ActorViewSet, DirectorViewSet, ActorFilmsViewSet, BestMovieViewSet, \
    ClosestBirthdaysActorViewSet, DirectorFilmsViewSet

urlpatterns = [
    # path('', views.home, name = 'home'),
    # path('movie/', views.movie, name = 'movie'),
    # path('director/', views.director, name = 'director'),
    # path('actor/', views.actor, name = 'actor'),
    # path('recommendation/', views.recommendation, name = 'recommendation'),
    # path('insert_data/', views.insert_data, name = 'insert_data'),
    # path('insert_data_submission/', views.insert_data_submission, name = 'insert_data_submission'),
    # path('new_movie/', views.new_movie, name='new_movie'),
    # url(r'^edit_movie/(?P<pk>\d+)/$', views.edit_movie, name='edit_movie'),
    # url(r'^delete_movie/(?P<pk>\d+)/$', views.delete_movie, name='delete_movie'),
    path('api/movies/', MovieViewSet.as_view(), name='movie-api'),
    path('api/movies/best/', BestMovieViewSet.as_view(), name='best-movies-api'),
    path('api/movies/best/<int:n>/', BestMovieViewSet.as_view(), name='best-n-movies-api'),
    path('api/actors/', ActorViewSet.as_view(), name='actor-api'),
    path('api/actors/birthdays/<str:date>/', ClosestBirthdaysActorViewSet.as_view(),
         name='closest-birthdays-actors-api'),
    path('api/directors/', DirectorViewSet.as_view(), name='director-api'),
    path('api/actors/<str:name>/films/', ActorFilmsViewSet.as_view(), name='actor-films-api'),
    path('api/directors/<str:name>/films/', DirectorFilmsViewSet.as_view(), name='director-films-api')
]
