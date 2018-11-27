from django.core.management.base import BaseCommand

starter_posts = [{
    'title': 
    'url': 
    'description': 
    'slug': 
    'author': 
}]

starter_comments = [{

}]

class Command(BaseCommand):
    help = "My shiny new management command."

    def add_arguments(self, parser):
        parser.add_argument('sample', nargs='+')

    def handle(self, *args, **options):
        raise NotImplementedError()
