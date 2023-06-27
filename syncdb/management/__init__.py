from django.core.management import load_command_class


def register_commands():
    load_command_class('syncdb', 'commands.syncdb')


register_commands()
