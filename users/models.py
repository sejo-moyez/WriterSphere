from django.db import models
from django.contrib.auth.models import Abstractuser

# Create your models here.
class User(Abstractuser):
  ROLE_CHOICES =[
    ('admin', 'admin'),
    ('writer', 'writer')
  ]
  role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='writer')

  def __str__(self):
      return self.username
  


