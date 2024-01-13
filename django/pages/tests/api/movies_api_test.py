from django.test import TestCase
from django.urls import reverse, NoReverseMatch
from rest_framework import status
from rest_framework.test import APIClient
from pages.models import Movie

class MovieAPITest(TestCase):
    def setUp(self):
        Movie.objects.create(title='Movie 1', year=2000, rating=9.0, metascore=80)
        Movie.objects.create(title='Movie 2', year=2010, rating=8.5, metascore=75)
        Movie.objects.create(title='Movie 3', year=2020, rating=8.8, metascore=85)

    def test_filter_by_start_year(self):
        url = reverse('movie-api')
        client = APIClient()

        response = client.get(url, {'start_year': 2010})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['results'][0]['title'], 'Movie 2')
        self.assertEqual(response.data['results'][1]['title'], 'Movie 3')

    def test_filter_by_end_year(self):
        url = reverse('movie-api')
        client = APIClient()

        response = client.get(url, {'end_year': 2010})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['results'][0]['title'], 'Movie 1')
        self.assertEqual(response.data['results'][1]['title'], 'Movie 2')

    def test_filter_by_start_and_end_year(self):
        url = reverse('movie-api')
        client = APIClient()

        response = client.get(url, {'start_year': 2000, 'end_year': 2010})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['results'][0]['title'], 'Movie 1')
        self.assertEqual(response.data['results'][1]['title'], 'Movie 2')

    def test_get_best_movies_default_n(self):
        url = reverse('best-movies')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 3)  # Assuming you have 3 movies in the setup

    def test_get_best_movies_with_n(self):
        url = reverse('best-n-movies', kwargs={'n': 2})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 2)

    def test_get_best_movies_with_invalid_n(self):
        with self.assertRaises(NoReverseMatch):
            url = reverse('best-n-movies', kwargs={'n': 'invalid'})
            self.client.get(url)
