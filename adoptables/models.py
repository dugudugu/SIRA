from django.db import models

# Models for adoptable dog instances
class Adoptable(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.TextField()
    age = models.CharField(max_length=100, default='unknown')
    breed = models.CharField(max_length=100, default='mix breed')
    
    FEMALE_DOG = 'Female'
    MALE_DOG = 'Male'
    sex = [(FEMALE_DOG, 'Female'), (MALE_DOG, 'Male')]
    
    ADOPTED = 'Adopted'
    NOT_ADOPTED = 'For Adoption'
    Satus = [(ADOPTED, 'Adopted'), (NOT_ADOPTED, 'For Adoption')]
    
    date_of_birth = models.CharField(max_length=100, default='unknown')
    in_shelter_from = models.CharField(max_length=100, default='')
    location = models.CharField(max_length=100, default='')
    
    dog_image1 = models.ImageField(upload_to='dog_images', blank=True)
    dog_image2 = models.ImageField(upload_to='dog_images', blank=True, null=True)
    
    def __str__(self):
        return self.name
    