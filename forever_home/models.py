from django.db import models
from django.urls import reverse


# Model for dogs who have been adopted
class HappyEnding(models.Model):
    name = models.CharField(max_length=100, default='')
    adoption_date = models.CharField(max_length=20, default='')
    adoption_image = models.ImageField(upload_to='adoption_images/', blank=True)
    
    def __str__(self):
        return self.name
    