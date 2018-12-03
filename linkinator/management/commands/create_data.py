from django.core.management.base import BaseCommand
from linkinator.models import Post, Comment, Vote
from django.contrib.auth.models import User
from mimesis import Person, Generic, locales
import random

class Command(BaseCommand):
    help = "My shiny new management command."

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print('Deleting Posts...')
        Post.objects.all().delete()

        print('Deleting users...')
        User.objects.filter(is_superuser=False).delete()

        person = Person()
        generic = Generic(locales.EN)

        users = []
        for fake_user in range(100):
            fake_user = User.objects.create_user(person.username(), person.email(), 'password')
            users.append(fake_user)
        print(f'{len(users)} users imported!!!')

        starter_posts = []
        for i in range(100):
            dictionary = {
                'title': (generic.text.title() + str(i)),
                'url': 'https://www.google.com',
                'description': generic.text.sentence(),
                'author': users[random.randrange(100)],
            }
            starter_posts.append(dictionary)
        print('Dictionary of posts successfuly created')

        posts = []
        for post_data in starter_posts:
            post = Post.objects.create(**post_data)
            posts.append(post)
        print(f'{len(posts)} Posts imported!!!')

        for i in range(200):
            Comment.objects.create(post=posts[random.randrange(100)], user=users[random.randrange(100)], comment=generic.text.sentence())
        print('200 comments imported!!!')

        for i in range(100):
            Vote.objects.create(post=posts[random.randrange(40)], user=users[i])
        print('100 votes imported!!!')
