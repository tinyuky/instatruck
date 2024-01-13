from django.test import TestCase
from django.urls import reverse, NoReverseMatch
from rest_framework import status
from pages.models import Actor

class ClosestBirthdaysActorViewSetTests(TestCase):
    def setUp(self):
        Actor.objects.create(name='Actor 1', date='1981-10-21')
        Actor.objects.create(name='Actor 3', date='1975-03-13')

    def test_get_closest_birthdays_actors(self):
        date_str = '1981-10-22'
        url = reverse('closest-birthdays-actors-api', kwargs={'date': date_str})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

        birthdates = [actor['birthdate'] for actor in response.data['results']]
        expected_order = ['1981-10-21', '1975-03-13']
        self.assertEqual(birthdates, expected_order)

    def test_get_closest_birthdays_actors_invalid_date_format(self):
        url = reverse('closest-birthdays-actors-api', kwargs={'date': '22-10-1981'})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_closest_birthdays_actors_missing_date(self):
        with self.assertRaises(NoReverseMatch):
            url = reverse('closest-birthdays-actors-api', kwargs={})
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
