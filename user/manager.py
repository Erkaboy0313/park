# from django.db.models import 
from django.contrib.auth.models import BaseUserManager


class DriverManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type='driver')

class AdminManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type='admin')

class OwnerManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type='owner')


