from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class profile (models.Model):
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')
    user=models.OneToOneField(User,on_delete=models.CASCADE)

class Football(models.Model):
        title = models.CharField(max_length=100)

        content = models.TextField()
        time=models.DateTimeField(default=timezone.now)
        def __str__(self):
            return self.title

