import uuid
import hashlib

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    public_id = models.UUIDField(default=uuid.uuid4, editable=False)
    email = models.EmailField(blank=False, unique=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    @property
    def raw_password(self):
        raise AttributeError("Password cannot be read")

    @raw_password.setter
    def raw_password(self, raw_pass):
        self._password = self.set_password(raw_pass)

    def create_gravatar(self):
        gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(
            bytes(self.email.lower(),
            encoding='utf-8')
        ).hexdigest() + "?"
        
        return gravatar_url

    def save_user(self):
        self.save()