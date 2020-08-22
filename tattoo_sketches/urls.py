
'''
from django.urls import path
from . import views
from .views import sketches

urlpatterns = [

    # path('gallery_sketches.html', views.sketches, name="gallery_sketches"),
    path('gallery_sketches.html', sketches)
]

from django.urls import path
from . import views

urlpatterns = [

    path('gallery_sketches.html', views.sketches(), name="gallery_sketches"),

]
'''