from django.db import models
from django.urls import reverse

# Models for adoptable dog instances
class Adoptable(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.TextField()
    age = models.CharField(max_length=100, default='unknown')
    breed = models.CharField(max_length=100, default='mix breed')
    
    sex = models.CharField(max_length=100, default='')
    
    SMALL = 'Small'
    MEDIUM = 'Medium'
    LARGE = 'Large'
    size =[(SMALL, 'Small'), (MEDIUM, 'Medium'), (LARGE, 'Large')]
    
    ADOPTED = 'Adopted'
    FOSTERED = 'Fostered'
    SHELTER = 'Shelter'
    situation = [(ADOPTED, 'Adopted'), (FOSTERED, 'Fostered'), (SHELTER, 'Shelter')]
    
    status = models.BooleanField(verbose_name='For adoption', default=True)
    date_of_birth = models.CharField(max_length=100, default='unknown')
    in_shelter_from = models.CharField(max_length=100, default='')
    location = models.CharField(max_length=100, default='')
    
    dog_image1 = models.ImageField(upload_to='dog_images', blank=True)
    dog_image2 = models.ImageField(upload_to='dog_images', blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse('dog_details', kwargs={'id':self.id})
    
    def __str__(self):
        return self.name
    
    