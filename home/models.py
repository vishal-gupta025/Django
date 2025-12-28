from django.db import models

# Create your models here.
class user_detailes(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=15)


from django.conf import settings

class Profile(models.Model):
    """Lightweight profile linked to Django's User model."""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"Profile({self.user.get_username()})"
    