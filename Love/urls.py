from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from apps.nurai.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index-page'),
    path('', include('apps.base.urls')),
    path('nurai/', include('apps.nurai.urls')),
    path('flag/', include('apps.flag.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
