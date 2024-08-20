from django.db import models
import uuid

class Account(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    register_from = models.CharField(max_length=10, choices=[('default', 'default'), ('facebook', 'facebook'), ('google', 'google'), ('apple', 'apple')], default='default')
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    email_verified_at = models.DateTimeField(null=True, blank=True)
    password = models.CharField(max_length=255)
    avatar = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('unknown', 'unknown'), ('male', 'male'), ('female', 'female')], default='unknown')
    birthday = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    zipcode = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=120, null=True, blank=True)
    address = models.CharField(max_length=512, null=True, blank=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    following_count = models.PositiveIntegerField(default=0)
    follower_count = models.PositiveIntegerField(default=0)
    remember_token = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.name
