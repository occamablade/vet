from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls', namespace='uesrs')),
    path('auth/', include('django.contrib.auth.urls')),
    path('about/', include('about.urls', namespace='about')),
    path('', include('pets.ursl', namespace='pets'))
]

handler404 = 'core.views.page_not_found'
handler403 = 'core.views.permission_denied'
handler500 = 'core.views.server_error'
