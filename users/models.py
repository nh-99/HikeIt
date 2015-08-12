from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)

class HikeItUserManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name):
        user = self.create(email=email)
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return user

    def create_superuser(self, email, password, first_name, last_name):
        user = self.create(email=email)
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.role = "admin"
        user.save()
        return user

class HikeItUser(AbstractBaseUser):
    objects = HikeItUserManager()
    
    username = models.CharField(max_length=254, unique=True, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True, blank=True)
    role = models.CharField(max_length=30, default="member")
    image = models.CharField(max_length=200, blank=True)
    token = models.CharField(max_length=300, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
