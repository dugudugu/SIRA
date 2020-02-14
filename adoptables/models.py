from django.db import models
from django.db.models import Q
from django.urls import reverse


class DogSearchManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(name__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs


# Model for adoptable dog instance
class Adoptable(models.Model):
    name = models.CharField(max_length=100, default='')
    in_shelter_from = models.CharField(max_length=20, default='')
    date_of_birth = models.CharField(max_length=20, default='')
    age = models.CharField(max_length=100, default='')
    breed = models.CharField(max_length=100, default='')
    
    FEMALE = 'Female'
    MALE = 'Male'
    SEX_CHOICES = [(FEMALE, 'Female'), (MALE, 'Male'),]
    sex = models.CharField(max_length=100, choices=SEX_CHOICES, default=FEMALE,)
    
    SMALL = 'Small'
    MEDIUM = 'Medium'
    LARGE = 'Large'
    SIZE_CHOICES = [(SMALL, 'Small'), (MEDIUM, 'Medium'), (LARGE, 'Large'),]
    size =models.CharField(max_length=100, choices=SIZE_CHOICES, default=SMALL)
    
    AT_FOSTER_FAMILY = 'At foster family'
    IN_SHELTER = 'In shelter'
    SITUATION_CHOICES = [(AT_FOSTER_FAMILY, 'At foster family'), (IN_SHELTER, 'In shelter'),]
    situation = models.CharField(max_length=100, choices=SITUATION_CHOICES, default='In shelter')
    
    status = models.BooleanField(verbose_name='For adoption')
    
    SPAIN = 'Spain'
    THE_NETHERLANDS = 'The Netherlands'
    LOCATION_CHOICES = [(SPAIN, 'Spain'), (THE_NETHERLANDS, 'The Netherlands'),]
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES ,default=SPAIN)
    
    description = models.TextField()
    
    dog_image1 = models.ImageField(upload_to='dog_images/', blank=True)
    dog_image2 = models.ImageField(upload_to='dog_images/', blank=True, null=True)
    dog_image3 = models.ImageField(upload_to='dog_images/', blank=True, null=True)
    dog_image4 = models.ImageField(upload_to='dog_images/', blank=True, null=True)

    objects = DogSearchManager()
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dog_details', kwargs={'pk':self.pk})
