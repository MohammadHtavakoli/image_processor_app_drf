from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProcessedImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_image = models.ImageField(upload_to='original/')
    processed_image = models.ImageField(upload_to='processed/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s image - {self.created_at}"