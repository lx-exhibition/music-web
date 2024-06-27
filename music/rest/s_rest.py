# rest serializers

from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import User
from ..models import m_major

class S_auth_User(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class S_User(ModelSerializer):
    class Meta:
        model = m_major.User
        fields = '__all__'

class S_Artist(ModelSerializer):
    class Meta:
        model = m_major.Artist
        fields = '__all__'

class S_Album(ModelSerializer):
    class Meta:
        model = m_major.Album
        fields = '__all__'

class S_Song(ModelSerializer):
    class Meta:
        model = m_major.Song
        fields = '__all__'

class S_PlayList(ModelSerializer):
    class Meta:
        model = m_major.PlayList
        fields = '__all__'

class S_Video(ModelSerializer):
    class Meta:
        model = m_major.Video
        fields = '__all__'

class S_Image(ModelSerializer):
    class Meta:
        model = m_major.Image
        fields = '__all__'

class S_Event(ModelSerializer):
    class Meta:
        model = m_major.Event
        fields = '__all__'

class S_Location(ModelSerializer):
    class Meta:
        model = m_major.Location
        fields = '__all__'

class S_SongRecord(ModelSerializer):
    class Meta:
        model = m_major.SongRecord
        fields = '__all__'

class S_VideoRecord(ModelSerializer):
    class Meta:
        model = m_major.VideoRecord
        fields = '__all__'

class S_ArtistTag(ModelSerializer):
    class Meta:
        model = m_major.ArtistTag
        fields = '__all__'

class S_AlbumTag(ModelSerializer):
    class Meta:
        model = m_major.AlbumTag
        fields = '__all__'

class S_SongTag(ModelSerializer):
    class Meta:
        model = m_major.SongTag
        fields = '__all__'

class S_PlayTag(ModelSerializer):
    class Meta:
        model = m_major.PlayTag
        fields = '__all__'

class S_VideoTag(ModelSerializer):
    class Meta:
        model = m_major.VideoTag
        fields = '__all__'

class S_Message(ModelSerializer):
    class Meta:
        model = m_major.Message
        fields = '__all__'

class S_AlbumComment(ModelSerializer):
    class Meta:
        model = m_major.AlbumComment
        fields = '__all__'

class S_SongComment(ModelSerializer):
    class Meta:
        model = m_major.SongComment
        fields = '__all__'

class S_PlayComment(ModelSerializer):
    class Meta:
        model = m_major.PlayComment
        fields = '__all__'

class S_VideoComment(ModelSerializer):
    class Meta:
        model = m_major.VideoComment
        fields = '__all__'

class S_EventComment(ModelSerializer):
    class Meta:
        model = m_major.EventComment
        fields = '__all__'

