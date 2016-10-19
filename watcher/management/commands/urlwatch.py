from django.core.management import BaseCommand

from watcher.watcher import cron

class Command(BaseCommand):
    # Show this when the user types help
    help = "Watch all the subscribed URLs and notify if changed"

    def handle(self, *args, **options):
        cron()
        
