from django.contrib import admin
from django.urls import path, include

from tattoo_gallery import views as gallery_views
from tattoo_sketches import views as skatches_views
from blog import views as blog_views
from django.conf import settings

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web_UVXTS.urls')),

    path('gallery.html', gallery_views.gallery, name="gallery"),
    path('gallery_sketches.html', skatches_views.sketches, name="gallery_sketches"),
    #   path('blog.html', blog_views.all_blogs, name="blog.html"),
     path('blog/', include('blog.urls'))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





