from django.db import models
from api.models.base import Base

class Device(Base):
    status = models.IntegerField(default=0)
    device_uid = models.CharField(max_length=255, default='')
    user = models.ForeignKey('auth.User', related_name='devices')

    def save(self, *args, **kwargs):
        super(Device, self).save(*args, **kwargs)
