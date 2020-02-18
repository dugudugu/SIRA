import django_filters
from adoptables.models import Adoptable

class DogSearchFilter(django_filters.FilterSet):
    class Meta:
        model = Adoptable
        fields = ['name',]