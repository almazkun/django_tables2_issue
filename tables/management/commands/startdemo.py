from django.core.management.base import BaseCommand
from tables.models import Conversation


class Command(BaseCommand):
    help = "Starts the demo"

    def handle(self, *args, **options):
        for i in range(1, 51):
            Conversation.objects.create(
                name=f"Conversation {i}",
                description=f"Description {i}",
            )
        self.stdout.write(self.style.SUCCESS("Demo started"))
