
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')), 
     path('accounts/', include('django.contrib.auth.urls'))  # Include the URLs from the core app
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
