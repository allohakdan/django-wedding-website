from django.core.management import BaseCommand
from guests import csv_import


class Command(BaseCommand):
    #args = 'filename'

    def add_arguments(self, parser):
        parser.add_argument('filename')

    def handle(self, filename, *args, **kwargs):
        csv_import.import_guests(filename)
