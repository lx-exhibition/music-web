from django.urls import path, re_path, include
from utils.decorators import to_text, to_html, to_template
from ..views import *

urlpatterns = [
    # path('', to_html('<h1>hello example app!</h1>')),
    path('', to_html('index.html'), name='index'),
    path('hello/', v_index.index),

    path('login/', v_auth._login, name='auth-login'),
    path('register/', v_auth._register, name='auth-register'),
    path('logout/', v_auth._logout, name='auth-logout'),

    path('upload/', v_index.upload, name="upload"),
    path('img/', v_index.img),
    re_path('img/(?P<path>.*)', v_index.img),

    re_path('test/', v_index.test, name='test'),
]
