from django.shortcuts import render
from .models import Sketches
from .filters import SketchesFilter

# Create your views here.
def sketches(request):
    sketches = Sketches.objects.all()
    myFilter = SketchesFilter(request.GET, queryset=sketches)
    filtered = SketchesFilter(request.GET, queryset=sketches)
    sketches = myFilter.qs

    context = {
        'sketches': sketches,
        'filtered': filtered,
        'myFilter': myFilter,
            }
    return render(request, 'gallery_sketches.html', context)

