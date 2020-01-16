from django.db import models


class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    country = models.CharField(max_length=40, blank=False)
    email = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return "{0}-{1}".format(self.id, self.full_name)