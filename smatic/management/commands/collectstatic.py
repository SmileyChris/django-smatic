from django.contrib.staticfiles.management.commands.collectstatic import \
    Command as StaticfilesCommand

from smatic.management.commands import extra_ignores


class Command(StaticfilesCommand):
    pass


extra_ignores(Command)
