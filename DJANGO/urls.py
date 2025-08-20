"""
URL configuration for DJANGO project.
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # This path connects the root URL of your site to the create_account_view.
    # The 'name' is crucial for the redirect in your view to work correctly.
    path('', views.create_account_view, name='create_account'),
]

# This is required to serve media files (like the profile picture) during development.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

