from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Тестова команда"

    def handle(self, *args, **kwargs):
        self.stdout.write("Работи!")
