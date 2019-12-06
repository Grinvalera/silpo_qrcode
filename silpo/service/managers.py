from django.db import models


class QRcodeManager(models.Manager):
    def get_queryset(self):
        return super(QRcodeManager, self).get_queryset().filter(is_active=True)