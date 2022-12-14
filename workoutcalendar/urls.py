


from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = []

if settings.ADMIN_ENABLED is True:
    urlpatterns += [path('admin/', admin.site.urls), ]

urlpatterns += [
    path('', include('frontend.urls')),
]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
