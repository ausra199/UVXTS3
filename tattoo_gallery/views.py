from django.shortcuts import render
from .models import Gallery

# Create your views here.
def gallery(request):
    gallery = Gallery.objects.order_by('-date')

    context = {
        'gallery': gallery
            }
    return render(request, 'gallery.html', context)

