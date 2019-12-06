from django.db import models
import uuid
from .choices import STATUSES
from .managers import QRcodeManager


class QRCode(models.Model):
    image = models.ImageField(upload_to='')
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    zone = models.ForeignKey('QrZone', on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)
    objects = models.Manager()
    active_objects = QRcodeManager()

    def __str__(self):
        return f'{self.zone.name}'


class QrZone(models.Model):
    name = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'


class Feedback(models.Model):
    qr_id = None
    text = models.CharField(max_length=512)
    name = models.CharField(max_length=128, blank=True)
    contact = models.CharField(max_length=48, blank=True)
    status = models.IntegerField(choices=STATUSES, default=1)

    def __str__(self):
        return f'{self.name}'

# Create your models here.
