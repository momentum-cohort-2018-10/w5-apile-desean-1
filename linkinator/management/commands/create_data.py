from django.core.management.base import BaseCommand
from linkinator.models import Post, Comment, Vote, Favorite
from django.contrib.auth.models import User
from mimesis import Person
from linkinator.models import Post, Comment, Vote, Favorite

class Command(BaseCommand):
    help = "My shiny new management command."

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print('Deleting Posts...')
        Post.objects.all().delete()

        print('Deleting users...')
        User.objects.filter(is_superuser=False).delete()

        users = []
        person = Person()
        for fake_user in range(100):
            fake_user = User.objects.create_user(person.username(), person.email(), 'password')
            users.append(fake_user)
        print(f'{len(users)} users imported!!!')


        import random

        starter_posts = []

        for i in range(100):
            dictionary = {
                'title': f'A craaaaaazzy title {i}',
                'url': 'https://www.google.com',
                'description': 'This is a simple post. We are simple people. Onomatopoeia...',
                'author': users[random.randrange(100)],
            }
            starter_posts.append(dictionary)

        posts = []
        for post_data in starter_posts:
            post = Post.objects.create(**post_data)
            posts.append(post)
        print(f'{len(posts)} Posts imported!!!')


        comments = []
        for i in range(90):
            Comment.objects.create(post=posts[random.randrange(90)], user=users[random.randrange(90)], comment='this is a comment. lorem ipsem in your face')

        for i in range(100):
            Vote.objects.create(post=posts[random.randrange(90)], user=users[i])
