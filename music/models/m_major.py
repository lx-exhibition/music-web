from django.db import models
from django.contrib.auth.models import User as auth_User, Permission
from django.db.models import TextField

from utils.coder import encode_upload_file, encode_upload_video, encode_upload_image, encode_upload_docs,encode_upload_music
import json
from pathlib import Path
cur_path = Path(__file__).resolve().parent


class User(models.Model):
    origin_user = models.OneToOneField(auth_User, on_delete=models.CASCADE)
    location = models.ForeignKey("Location", on_delete=models.CASCADE, blank=True, default=0, null=True)
    avatar = models.ForeignKey("Image", on_delete=models.CASCADE, blank=True, default=0)
    fans = models.ManyToManyField("User", related_name="concerns", blank=True)
    msg_users = models.ManyToManyField("User", related_name="msged_users", through="Message", blank=True)

    gender = models.IntegerField(choices={0: "未知", 1: "男", 2: "女"}, default=0)
    birthday = models.DateTimeField(blank=True, null=True)
    nickname = models.CharField(max_length=50, db_default="用户已注销")
    cellphone = models.CharField(max_length=20, blank=True, null=True)
    qq = models.CharField(max_length=20, blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    experience = models.IntegerField(default=0, db_default=0)

    def __str__(self):
        return f'{self.nickname}'


class Artist(models.Model):
    account = models.OneToOneField("User", on_delete=models.CASCADE)
    # avatar = models.ForeignKey("Image", on_delete=models.CASCADE, related_name="avatar_artists", blank=True, default=0)
    background = models.ForeignKey("Image", on_delete=models.CASCADE, related_name="background_artists", blank=True, default=0)

    stagename = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True, db_default="这家伙什么都没留下...")
    joined_time = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return f'{self.stagename}'

class Album(models.Model):
    artist = models.ForeignKey("Artist", on_delete=models.CASCADE, related_name="albums")
    background = models.ForeignKey("Image", on_delete=models.CASCADE, related_name="background_albums")
    collected_users = models.ManyToManyField("User", related_name="collected_albums")
    commented_users = models.ManyToManyField("User", related_name="commented_albums", through="AlbumComment")

    title = models.CharField(max_length=50)
    count = models.IntegerField(default=0, db_default=0)
    shared_count = models.IntegerField(default=0, db_default=0)
    liked_count = models.IntegerField(default=0, db_default=0)
    description = TextField()
    pub_company = models.CharField(max_length=50, blank=True, null=True)
    pub_date = models.DateField(blank=True, auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

class Song(models.Model):
    album = models.ForeignKey("Album", on_delete=models.CASCADE, related_name="songs")
    img = models.ForeignKey("Image", on_delete=models.CASCADE, related_name="songs")
    create_artists = models.ManyToManyField("Artist", related_name="created_songs")
    comment_users = models.ManyToManyField("User", related_name="commented_songs", through="SongComment")

    title = models.CharField(max_length=50)
    count = models.IntegerField(default=0)
    shared_count = models.IntegerField(default=0, db_default=0)
    liked_count = models.IntegerField(default=0, db_default=0)
    data = models.FileField(upload_to=encode_upload_music)
    lyrics = models.TextField(blank=True, null=True)
    pub_date = models.DateField(blank=True, auto_now_add=True)

    @staticmethod
    def generate_data(url):
        d = get(url).content
        return ContentFile(d, name=url.split('/')[-1])

    def __str__(self):
        return f'{self.title}'

class PlayList(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="playlists")
    img = models.ForeignKey("Image", on_delete=models.CASCADE, related_name="playlists")
    join_songs = models.ManyToManyField("Song", related_name="joined_playlists")
    collect_users = models.ManyToManyField("User", related_name="collected_playlists")
    comment_users = models.ManyToManyField("User", related_name="commented_playlists", through="PlayComment")

    title = models.CharField(max_length=50)
    count = models.IntegerField(default=0, db_default=0)
    shared_count = models.IntegerField(default=0, db_default=0)
    liked_count = models.IntegerField(default=0, db_default=0)
    description = models.TextField()
    pub_date = models.DateField(blank=True, auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

class Video(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="videos")
    img = models.ForeignKey("Image", on_delete=models.CASCADE, related_name="videos")
    collect_users = models.ManyToManyField("User", related_name="collected_videos")
    comment_users = models.ManyToManyField("User", related_name="commented_videos", through="VideoComment")

    title = models.CharField(max_length=50)
    count = models.IntegerField(default=0, db_default=0)
    shared_count = models.IntegerField(default=0, db_default=0)
    liked_count = models.IntegerField(default=0, db_default=0)
    description = models.TextField(blank=True, null=True)
    data = models.FileField(upload_to=encode_upload_video)
    pub_date = models.DateField(blank=True, auto_now_add=True)

    @staticmethod
    def generate(url,**kwargs):
        d = get(url).content
        obj = Video.objects.create(data=ContentFile(d, name=url.split('/')[-1]),**kwargs)
        return obj.id

    def __str__(self):
        return f'{self.title}'


from requests import get
from django.core.files.base import ContentFile
class Image(models.Model):
    data = models.ImageField(upload_to=encode_upload_image)

    @staticmethod
    def generate(url):
        d = get(url).content
        obj = Image.objects.create(data=ContentFile(d, name=url.split('/')[-1]))
        return obj.id

class Event(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="events")
    comment_users = models.ManyToManyField("User", related_name="commented_events", through="EventComment")

    shared_count = models.IntegerField(default=0, db_default=0)
    liked_count = models.IntegerField(default=0, db_default=0)
    content = models.TextField()
    pub_date = models.DateField(auto_now_add=True, blank=True)

class Location(models.Model):
    # province = models.CharField(max_length=6)
    # city = models.CharField(max_length=8)
    code = models.SmallIntegerField(unique=True)
    location = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.location}({self.code})"

    @staticmethod
    def generate():
        data = []
        with open(f'{cur_path}/data/location.json','r',encoding='utf-8') as f:
            data = json.loads(f.read())
            print(data)

        for v in data:
            Location.objects.create(code=v[0], location=v[1])

class SongRecord(models.Model):
    song = models.ForeignKey("Song", on_delete=models.CASCADE, related_name="recorded_songs")
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="played_songs")

    count = models.IntegerField(default=1, db_default=1)
    last_time = models.DateTimeField(blank=True, auto_now=True)

    class Meta:
        unique_together = ("song", "user")

class VideoRecord(models.Model):
    video = models.ForeignKey("Video", on_delete=models.CASCADE, related_name="recorded_videos")
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="played_videos")

    count = models.IntegerField(default=1, db_default=1)
    last_time = models.DateTimeField(blank=True, auto_now=True)

    class Meta:
        unique_together = ("video", "user")

class ArtistTag(models.Model):
    tag_artists = models.ManyToManyField("Artist", related_name="seted_tags")

    tag = models.CharField(max_length=10)
    subtag = models.CharField(max_length=10)

    class Meta:
        unique_together = ("tag", "subtag")

    @staticmethod
    def generate():
        data = []

        with open(f'{cur_path}/data/artist_tag.json','r',encoding='utf-8') as f:
            data = json.loads(f.read())
            print(data)

        for v in data:
            ArtistTag.objects.create(tag=v[0], subtag=v[1])

class AlbumTag(models.Model):
    tag_albums = models.ManyToManyField("Album", related_name="seted_tags")

    tag = models.CharField(max_length=10)
    subtag = models.CharField(max_length=10)

    class Meta:
        unique_together = ("tag", "subtag")

class SongTag(models.Model):
    tag_songs = models.ManyToManyField("Song", related_name="seted_tags")

    tag = models.CharField(max_length=10)
    subtag = models.CharField(max_length=10)

    class Meta:
        unique_together = ("tag", "subtag")

class PlayTag(models.Model):
    tag_songlists = models.ManyToManyField("PlayList", related_name="seted_tags")

    tag = models.CharField(max_length=10)
    subtag = models.CharField(max_length=10)

    class Meta:
        unique_together = ("tag", "subtag")

    @staticmethod
    def generate():
        data = []
        with open(f'{cur_path}/data/playtag.json', 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
            print(data)
        for v in data:
            PlayTag.objects.create(tag=v[0], subtag=v[1])

class VideoTag(models.Model):
    tag_videos = models.ManyToManyField("Video", related_name="seted_tags")

    tag = models.CharField(max_length=10)


    @staticmethod
    def generate():
        data = []
        with open(f'{cur_path}/data/videotag.json', 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
            print(data)
        for v in data:
            VideoTag.objects.create(tag=v)

class Message(models.Model):
    send_user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="sended_messages")
    receive_user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="received_messages")

    content = TextField()
    send_time = models.DateTimeField(blank=True, auto_now_add=True)


class AlbumComment(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="album_comments")
    album = models.ForeignKey("Album", on_delete=models.CASCADE, related_name="comments")

    content = models.TextField()
    shared_count = models.IntegerField(default=0, db_default=0)
    liked_count = models.IntegerField(default=0, db_default=0)
    pub_time = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return f'{self.content}'

class SongComment(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="song_comments")
    song = models.ForeignKey("Song", on_delete=models.CASCADE, related_name="comments")

    content = models.TextField()
    shared_count = models.IntegerField(default=0, db_default=0)
    liked_count = models.IntegerField(default=0, db_default=0)
    pub_time = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return f'{self.content}'

class PlayComment(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="play_comments")
    playlist = models.ForeignKey("PlayList", on_delete=models.CASCADE, related_name="comments")

    content = models.TextField()
    shared_count = models.IntegerField(default=0, db_default=0)
    liked_count = models.IntegerField(default=0, db_default=0)
    pub_time = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return f'{self.content}'

class VideoComment(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="video_comments")
    video = models.ForeignKey("Video", on_delete=models.CASCADE, related_name="comments")

    content = models.TextField()
    shared_count = models.IntegerField(default=0, db_default=0)
    liked_count = models.IntegerField(default=0, db_default=0)
    pub_time = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return f'{self.content}'

class EventComment(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="event_comments")
    event = models.ForeignKey("Event", on_delete=models.CASCADE, related_name="comments")

    content = models.TextField()
    shared_count = models.IntegerField(default=0, db_default=0)
    liked_count = models.IntegerField(default=0, db_default=0)
    pub_time = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return f'{self.content}'


