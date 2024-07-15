from .models import Region, PowerOutageLog, User
from .utils import send_power_outage_email
from django.utils import timezone

# Function ini adalah untuk menjalankan pengecekan status power di masing2 region
# Jika status power di suatu region false, maka akan melakukan proses pengiriman email notifikasi
def check_power_status():
    regions = Region.objects.all()
    for region in regions:
        if not region.status:
            log = PowerOutageLog.objects.create(region=region, status=False)
            users = User.objects.filter(region=region)
            for user in users:
                send_power_outage_email(user.email, region.name)
                log.notified = True
            log.save()
