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


# Model for dogs who have been adopted
class HappyEnding(models.Model):
    name = models.CharField(max_length=100, default='')
    status = models.BooleanField(verbose_name='For adoption', default='False')
    adoption_date = models.CharField(max_length=20, default='')
    adoption_image = models.ImageField(upload_to='adoption_images/', blank=True)
    
    objects = DogSearchManager()
    
    def __str__(self):
        return self.name
    