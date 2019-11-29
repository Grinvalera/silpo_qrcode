from django.db import models


class QRCode(models.Model):
    pass


class QrZone(models.Model):
    name = models.CharField(max_length=128)


class Feedback(models.Model):
    qr_id = None
    text = models.CharField(max_length=512)
    name = models.CharField(max_length=128)
    contact = models.CharField(max_length=48)

# Create your models here.
