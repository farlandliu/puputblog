from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('puput.urls')),
]

urlpatterns += static(settings.MEDIA_URL + 'images/', document_root=os.path.join(settings.MEDIA_ROOT, 'images'))

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


if settings.DEBUG:
    import os
    from django.views.generic.base import RedirectView
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns() # tell gunicorn where static files are in dev mode
    urlpatterns += static(settings.MEDIA_URL + 'images/', document_root=os.path.join(settings.MEDIA_ROOT, 'images'))
    urlpatterns += [
        path(r'favicon\.ico', RedirectView.as_view(url=settings.STATIC_URL + 'favicon.ico')),
    ]