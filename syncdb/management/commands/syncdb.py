from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Custom syncdb command'

    def handle(self, *args, **options):
        # Hier kannst du die Logik für den Export und Import der Datenbank implementieren
        self.stdout.write(self.style.SUCCESS('Datenbank synchronisiert.'))
