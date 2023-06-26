#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
""" from django.core.management.base import BaseCommand
from board.models import Database """


""" if __name__ == "__main__": """
# Run administrative tasks.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Joinbackend.settings')
# try:
#   from django.core.management import execute_from_command_line
# except ImportError as exc:
# raise ImportError(
# from import_export import resources
# from import_export.fields import Field
#   "Couldn't import Django. Are you sure it's installed and "
#  "available on your PYTHONPATH environment variable? Did you "
#  "forget to activate a virtual environment?"
# ) from exc
# execute_from_command_line(sys.argv)




import os
import sys
def main():
    # Run administrative tasks.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Joinbackend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


""" class DatabaseResource(resources.ModelResource):
    class Meta:
        model = Database
 """

""" class Command(BaseCommand):
    help = 'Migrates data from local database to PythonAnywhere database'

    def migrate_data(self):
        dataset = DatabaseResource().export() """

# Hier kommt der Code, um die Daten in die neue Datenbank zu importieren
# for row in dataset:
#  database = Database()
#  database.id = row['id']
# database.username = row['username']
# database.first_name = row['first_name']
# database.last_name = row['last_name']
# database.email = row['email']
# database.color = row['color']
# database.save()

# def handle(self, *args, **options):
# self.migrate_data()
