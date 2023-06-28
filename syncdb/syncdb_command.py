from django.core.management.base import BaseCommand
from dbbackup.management.commands.dbbackup import Command as DbBackupCommand
from dbbackup.management.commands.dbrestore import Command as DbRestoreCommand


class Command(BaseCommand):
    help = 'Synchronize the database by exporting and importing data.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--backup-path', help='Path to store the database backup.')

    def handle(self, *args, **options):
        # Export database
        backup_path = options.get('backup_path', '')
        db_backup_command = DbBackupCommand()
        db_backup_command.handle(outputfile=backup_path)

        # Import database
        db_restore_command = DbRestoreCommand()
        db_restore_command.handle(database=backup_path)
