from django.urls import path,re_path
from music.apis import v_api
from music.apis import v_test



urlpatterns = [
    # re_path('^img/(?P<path>.*)$', v_test.img),
    path('mail/', v_test.send_mail),

    path('auth-user/', v_api.crud_AuthUser),
    path('user/', v_api.crud_user),
    path('Artist/', v_api.crud_Artist),
    path('Album/', v_api.crud_Album),
    path('Song/', v_api.crud_Song),
    path('PlayList/', v_api.crud_PlayList),
    path('Video/', v_api.crud_Video),
    path('Image/', v_api.crud_Image),
    path('Event/', v_api.crud_Event),
    path('Location/', v_api.crud_Location),
    path('SongRecord/', v_api.crud_SongRecord),
    path('VideoRecord/', v_api.crud_VideoRecord),
    path('ArtistTag/', v_api.crud_ArtistTag),
    path('AlbumTag/', v_api.crud_AlbumTag),
    path('SongTag/', v_api.crud_SongTag),
    path('PlayTag/', v_api.crud_PlayTag),
    path('VideoTag/', v_api.crud_VideoTag),

    re_path('.*', v_api.NOTFOUND),
]
