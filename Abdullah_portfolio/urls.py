from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appport.urls')),  # Aapki appport ke URLs
    path('dproject/', include('dproject.urls')),  # Aapke dproject ke URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Authentication URLs include karna
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
