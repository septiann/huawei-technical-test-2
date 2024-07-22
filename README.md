# Huawei Technical Test - 2

Aplikasi ini digunakan untuk memonitor pemadaman listrik di wilayah tertentu yang terdaftar di dalam database dan mengirimkan email pemberitahuan secara otomatis.

## Requirements

- Python: 3.11.5
- Django 5.0.7
- PostgreSQL
- MailTrap (untuk test email hosting)
- Crontab (untuk melakukan job automation)

## Installation

### Clone Repo
```
git clone https://github.com/septiann/huawei-technical-test-2.git
cd huawei-technical-test-2
```

### Install dependency
```
pip install django psycopg2-binary
```

### Configuration
- Database
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'power_monitor_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
```
python manage.py migrate
```

- Email Configuration
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = '' # username smtp
EMAIL_HOST_PASSWORD = '' # password smtp
EMAIL_PORT = '2525'
```

- Automation Job
Untuk menjadwalkan monitoring, tambahkan konfigurasi berikut di dalam `settings.py`
```
CRONJOBS = [
    ('*/5 * * * *', 'monitoring.tasks.check_power_status', f'>> {BASE_DIR}/monitoring/logs/check_power_status.log 2>&1'),
]
```
Sebagai contoh, jalankan job setiap 5 menit sekali di menit ke-5 dan kelipatannya. Sebagai catatan, di dalam sistem anda harus terlebih dahulu terinstall aplikasi Crontab.

### Running Server
```
python manage.py runserver
```

## Unit Testing
```
python manage.py test
```


## Functions
### Tasks
`check_power_status`
Fungsi ini digunakan untuk memeriksa status listrik di setiap wilayah yang terdaftar dan akan membuat log jika terjadi pemadaman. Jika ditemukan wilayah yang mengalami pemadaman, fungsi ini juga akan mengirim email notifikasi kepada pengguna yang terdaftar di wilayah tersebut.

### Utils
`send_power_outage_email`
Fungsi ini digunakan untuk mengirim email notifikasi pemadaman listrik kepada pengguna.
