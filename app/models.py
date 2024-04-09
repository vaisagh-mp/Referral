from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    referral_code = models.CharField(max_length=10, blank=True, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        related_query_name='custom_user',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        related_query_name='custom_user',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

class Referral(models.Model):
    referrer = models.ForeignKey(User, related_name='referrals', on_delete=models.CASCADE)
    referred_user = models.ForeignKey(User, related_name='referred_by', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
