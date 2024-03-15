from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    is_owner = models.BooleanField(default=False)
    is_staff_member = models.BooleanField(default=False)

    class Meta:
        db_table = 'auth_user'
        swappable = 'AUTH_USER_MODEL'




class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='owner_profile')
    company_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.user.username


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staff_profile')
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.position} - {self.user.username}"

