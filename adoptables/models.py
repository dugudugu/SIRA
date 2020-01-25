from django.db import models
from django.urls import reverse


# Models for adoptable dog instances
class Adoptable(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.TextField()
    age = models.CharField(max_length=100, default='Unknown')
    breed = models.CharField(max_length=100, default='Mix breed')
    sex = models.CharField(max_length=100, default='')
    size =models.CharField(max_length=100, default='')
    situation = models.CharField(max_length=100, default='')
    status = models.BooleanField(verbose_name='For adoption', default=True)
    date_of_birth = models.CharField(max_length=100, default='Unknown')
    in_shelter_from = models.CharField(max_length=100, default='')
    location = models.CharField(max_length=100, default='')
    
    dog_image1 = models.ImageField(upload_to='dog_images/', blank=True)
    dog_image2 = models.ImageField(upload_to='dog_images/', blank=True, null=True)
    dog_image3 = models.ImageField(upload_to='dog_images/', blank=True, null=True)
    dog_image4 = models.ImageField(upload_to='dog_images/', blank=True, null=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dog_details', kwargs={'pk':self.pk})
    