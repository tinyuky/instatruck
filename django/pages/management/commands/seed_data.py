# seed_data.py

import random
from faker import Faker
from django.core.management.base import BaseCommand

from pages.models import Movie, Actor, Director

fake = Faker()

class Command(BaseCommand):
    help = 'Seed random data for Movie, Director, and Actor models'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Deleting existing data...'))
        self.delete_existing_data()

        self.stdout.write(self.style.SUCCESS('Seeding data...'))

        self.seed_directors()
        self.seed_actors()
        self.seed_movies()

        self.stdout.write(self.style.SUCCESS('Data seeding complete.'))

    def delete_existing_data(self):
        Movie.objects.all().delete()
        Director.objects.all().delete()
        Actor.objects.all().delete()

    def seed_movies(self):
        directors = Director.objects.all()
        actors = Actor.objects.all()

        for _ in range(10):
            director = random.choice(directors)
            actor = random.choice(actors)

            movie = Movie.objects.create(
                year=fake.year(),
                rank=fake.random_int(min=1, max=100),
                title=fake.sentence(),
                description=fake.text(max_nb_chars=500),
                duration=fake.random_int(min=60, max=180),
                genres=fake.word(),
                rating=fake.pyfloat(left_digits=1, right_digits=1, positive=True),
                metascore=fake.random_int(min=1, max=100),
                votes=fake.random_int(min=1, max=1000000),
                gross_earning_in_mil=fake.pyfloat(left_digits=2, right_digits=2, positive=True),
                director=director,
                actor=actor,
            )

    def seed_directors(self):
        for _ in range(10):
            Director.objects.create(
                name=fake.unique.name(),
                date=fake.date_of_birth(),
                place=fake.city(),
                masterpiece=fake.sentence(),
                award_win=fake.random_int(min=0, max=10),
                award_nom=fake.random_int(min=0, max=10),
                person_link=fake.url(),
                award_link=fake.url(),
            )

    def seed_actors(self):
        for _ in range(10):
            Actor.objects.create(
                name=fake.unique.name(),
                date=fake.date_of_birth(),
                place=fake.city(),
                masterpiece=fake.sentence(),
                award_win=fake.random_int(min=0, max=10),
                award_nom=fake.random_int(min=0, max=10),
                person_link=fake.url(),
                award_link=fake.url(),
            )
