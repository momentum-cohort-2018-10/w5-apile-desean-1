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
        for fake_user in range(10):
            fake_user = User.objects.create_user(person.username(), person.email(), 'password')
            users.append(fake_user)
        print("Users created")

        starter_posts = [
            {
                'title': 'First post',
                'url': 'https://www.google.com',
                'description': 'This is a simple post. We are simple people. Onomatopoeia...',
                'author': users[0],
            },
            {
                'title': 'Second post',
                'url': 'https://www.google.com',
                'description': 'This is a simple post. We are simple people. Onomatopoeia...',
                'author': users[0],
            },
            {
                'title': 'Third post',
                'url': 'https://www.google.com',
                'description': 'This is a simple post. We are simple people. Onomatopoeia...',
                'author': users[0],
            },
            {
                'title': 'Fourth post',
                'url': 'https://www.google.com',
                'description': 'This is a simple post. We are simple people. Onomatopoeia...',
                'author': users[0],
            },
            {
                'title': 'Fifth post',
                'url': 'https://www.google.com',
                'description': 'This is a simple post. We are simple people. Onomatopoeia...',
                'author': users[0],
            },
            {
                'title': 'Sixth post',
                'url': 'https://www.google.com',
                'description': 'This is a simple post. We are simple people. Onomatopoeia...',
                'author': users[0],
            },
        ]

        posts = []
        for post_data in starter_posts:
            post = Post.objects.create(**post_data)
            posts.append(post)
        print('Posts imported!!!')

        # Vote.objects.create(post=posts[0], user=users[0])
        # Vote.objects.create(post=posts[0], user=users[1])
        # Vote.objects.create(post=posts[0], user=users[2])
        # Vote.objects.create(post=posts[3], user=users[3])
        # Vote.objects.create(post=posts[3], user=users[4])
        # Vote.objects.create(post=posts[4], user=users[5])
        # Vote.objects.create(post=posts[4], user=users[6])
        # Vote.objects.create(post=posts[4], user=users[7])
        # Vote.objects.create(post=posts[4], user=users[8])
        # Vote.objects.create(post=posts[4], user=users[9])
