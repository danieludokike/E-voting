from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), # Django Admin
    
    # Own Apps routes
    path("", include("pollapp.urls")),
    path("account/pollapp/", include("account.urls")),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
