from django.conf import settings
from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, re_path
from graphene_django.views import GraphQLView

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^__status__/', lambda _: JsonResponse({'status': 'OK'})),
    re_path(r'^graphql', GraphQLView.as_view(graphiql=settings.GRAPHIQL_ENABLED))
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [re_path(r'^__debug__/', include(debug_toolbar.urls)), ] + urlpatterns
