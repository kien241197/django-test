from django.db import models

# Create your models here.
class Member(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()
  phone = models.IntegerField(null=True)
  note = models.TextField()
  joined_at = models.DateField(null=True)

  def __str__(self):
  	return f"{self.name} {self.email} {self.phone} {self.joined_at}"