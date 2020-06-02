from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('User Harus Memiliki Email')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password):
        """Buat dan Simpan Superuser baru"""
        user = self.create_user(email, password)
        user.is_start = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """custom user model"""
    email = models.EmailField(max_length=150, unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_start = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
