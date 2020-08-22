import django_filters
from .models import Sketches


class SketchesFilter(django_filters.FilterSet):
    class Meta:
        model = Sketches
        fields = ['type']

