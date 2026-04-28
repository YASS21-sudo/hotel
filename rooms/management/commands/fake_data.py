from django.core.management.base import BaseCommand
from faker import Faker
from rooms.models import RoomType, Room
import random

class Command(BaseCommand):
    help = 'Génère les données fictives pour les chambres'

    def handle(self, *args, **options):
        faker = Faker('fr_FR')

        categories = []
        for _ in range(5):
            name = faker.word().capitalize()
            slug = faker.slug(name)
            categorie = RoomType.objects.create(name=name, slug=slug)
            categories.append(categorie)
            self.stdout.write(f'Type de chambre créé avec succès : {name}')

        for i in range(8):
            Room.objects.create(
                name=faker.sentence(nb_words=4).replace('.', ''),
                description=faker.text(max_nb_chars=450),
                price=faker.random_number(digits=4),
                stock=faker.random_int(0, 100),
                category=random.choice(categories)
            )
            self.stdout.write(f'Chambre {i+1} créée avec succès')
