from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from music.views import v_index
from utils.decorators import to_text, to_html_raw, to_template, redirect_path
from . import settings


from graphene_django.views import GraphQLView

# /, /admin/, /media/, /static/ 默认是可访问的
urlpatterns = [
    path('', to_text('hello world'), name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path('e/', include('music.urls')),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}, "media"),
    # re_path(r"^api/img/(?P<path>.*)$", v_index.img),
    path("apis/", include('music.apis.u_api')),
    path("rest/", include('music.rest.u_rest')),

    # graphene-django
    path('graphql', GraphQLView.as_view(graphiql=True)),


    path('favicon.ico', redirect_path('/media/favicon.ico')),
    path('logo.ico', redirect_path('/media/logo.ico')),
    re_path(f"^.*$", to_text("<h1>404 Not Found</h1>", 404))
]

