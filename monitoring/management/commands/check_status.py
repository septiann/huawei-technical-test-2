from django.core.management.base import BaseCommand
from monitoring.tasks import check_power_status

class Command(BaseCommand):
    help = 'Check power status in all regions'

    def handle(self, *args, **kwargs):
        check_power_status()
