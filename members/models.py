from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Company(models.Model):
  name = models.CharField(max_length=255)
  address = models.CharField(max_length=255, null=True)
  note = models.TextField(null=True)
  created_at = models.DateField(null=True)

  def __str__(self):
  	return f"{self.name}"

class Member(AbstractUser):
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']

  name = models.CharField(max_length=255)
  email = models.EmailField(max_length=100, unique=True)
  phone = models.CharField(max_length=255, null=True)
  note = models.TextField(null=True)
  joined_at = models.DateField(null=True)
  password = models.CharField(max_length=100, null=True)
  company = models.ForeignKey(
    Company,
    on_delete=models.CASCADE,
    related_name='Company',
    null=True
  )

  def __str__(self):
  	return f"{self.name} {self.email} {self.phone} {self.joined_at} {self.company}"