import django_filters
from .models import Adoptable


class DogsFilter(django_filters.FilterSet):
    class Meta:
        model = Adoptable
        fields = ['sex', 'size', 'situation', 'location',]
        
    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
            super(DogsFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
            self.filters['sex'].field.widget.attrs.update({'class': 'input filter-size'})
            self.filters['size'].field.widget.attrs.update({'class': 'input filter-size'})
            self.filters['situation'].field.widget.attrs.update({'class': 'input filter-size'})
            self.filters['location'].field.widget.attrs.update({'class': 'input filter-size'})
            
