from django.db import models

class License(models.Model):
    key = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    expiration_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    is_admin = models.BooleanField(default=False)

# class AdminAction(models.Model):
#     action_type = models.CharField(max_length=255)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
