from django.contrib import admin
# from .models.m_index import Profile, Song, Artist, Song_Artist, Album, Movie
#
# admin.site.register(Profile)
# admin.site.register(Song)
# admin.site.register(Artist)
# admin.site.register(Song_Artist)
# admin.site.register(Album)
# admin.site.register(Movie)

from .models.m_major import User, Artist, Album, Song, PlayList, Video, Image, Event, Location
from .models.m_major import SongRecord, VideoRecord, AlbumTag, SongTag, VideoTag
from .models.m_major import Message, AlbumComment, SongComment, PlayComment, VideoComment, EventComment
admin.site.register(User)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(PlayList)
admin.site.register(Video)
admin.site.register(Image)
admin.site.register(Event)
admin.site.register(Location)
admin.site.register(SongRecord)
admin.site.register(VideoRecord)
admin.site.register(AlbumTag)
admin.site.register(SongTag)
admin.site.register(VideoTag)
admin.site.register(Message)
admin.site.register(AlbumComment)
admin.site.register(SongComment)
admin.site.register(PlayComment)
admin.site.register(VideoComment)
admin.site.register(EventComment)

