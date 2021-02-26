from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from teus import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('api/info/', include('info.urls')),
    path('api/user/', include('users.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)