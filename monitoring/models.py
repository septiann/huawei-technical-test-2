from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField()

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class PowerOutageLog(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()
    notified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.region.name} - {self.timestamp}"
