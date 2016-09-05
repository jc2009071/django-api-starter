from django.db import models
from django.contrib.auth.models import User
from api.models.base import Base

class UserCredential(Base):
    facebook_token = models.TextField(default='', unique=True)
    user = models.OneToOneField(User, related_name='facebook_token')
