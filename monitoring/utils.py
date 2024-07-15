from django.core.mail import send_mail
from django.conf import settings

# Function ini bertujuan untuk mengirim email yang mana terdapat 2 parameter yaiut email dan region
def send_power_outage_email(user_email, region_name):
    subject = f'Pemadaman Listrik di {region_name}'
    message = f'Pemberitahuan: Telah terjadi pemadaman listrik di wilayah {region_name}. Kami akan memberitahu Anda ketika listrik sudah kembali menyala.'
    email_from = 'admin@gmail.com'
    recipient_list = [user_email]
    send_mail(subject, message, email_from, recipient_list)