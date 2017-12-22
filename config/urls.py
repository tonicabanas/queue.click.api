from django.conf import settings
from django.urls import include, re_path
from django.contrib import admin
from django.http import JsonResponse

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^__status__/', lambda _: JsonResponse({'status': 'OK'}))
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [re_path(r'^__debug__/', include(debug_toolbar.urls)), ] + urlpatterns
