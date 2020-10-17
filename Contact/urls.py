
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Contact import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("app.urls")),
    path('', include("django.contrib.auth.urls")),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# customizing admin header text ..
admin.site.site_header = 'Contacts'
admin.site.index_title = 'Welcome to App'
admin.site.site_title = 'Control panel'
