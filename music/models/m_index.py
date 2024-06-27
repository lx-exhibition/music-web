# from django.db import models
# from django.contrib.auth.models import User
#
#
# # 用户信息
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#     fans = models.ManyToManyField(User, related_name='concerns')
#
#     def __str__(self):
#         return f'{self.user}\'s profile'
#
# class Song(models.Model):
#     name = models.CharField(max_length=50)
#     data = models.FileField(upload_to='uploads/%Y/%m/%d/')
#
#     artists = models.ManyToManyField("Artist", through="Song_Artist", related_name="songs")
#     album = models.ForeignKey("Album", on_delete=models.CASCADE, related_name="songs")
#     mv = models.ForeignKey("Movie", on_delete=models.CASCADE, related_name="songs")
#
#     def __str__(self):
#         return f"{self.name} [{self.album.name}]"
#
# from utils.coder import encode
#
# def avatar_path(instance, filename):
#     name = filename[:filename.rfind('.')]
#     ext = filename[filename.rfind('.') + 1:]
#     return f'avatars/{encode(name)}.{ext}'
# class Artist(models.Model):
#     name = models.CharField(max_length=50)
#     avatar = models.ImageField('图像', upload_to=avatar_path, blank=True, null=True)
#
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="artist")
#
#     def __str__(self):
#         return f"{self.name}  ({self.user})"
#
# class Song_Artist(models.Model):
#     song = models.ForeignKey("Song", on_delete=models.CASCADE)
#     artist = models.ForeignKey("Artist", on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.song}    [{self.artist.name}]"
#
# class Album(models.Model):
#     name = models.CharField(max_length=50)
#
#     artist = models.ForeignKey("Artist", on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.name}    [{self.artist.name}]"
#
#
# class Movie(models.Model):
#     name = models.CharField(max_length=50)
#     data = models.FileField(upload_to='uploads/%Y/%m/%d/')
#
#     def __str__(self):
#         return f'{self.name}'
#
#
# class A(models.Model):
#     bs = models.ManyToManyField("B",through="C")
# class B(models.Model):
#     pass
# from .utils import cur_time
# class C(models.Model):
#     a = models.ForeignKey("A", on_delete=models.CASCADE)
#     b = models.ForeignKey("B", on_delete=models.CASCADE)
#     sender = models.BooleanField(default=True)
#     msg = models.TextField("谈话", blank=False, null=True)
#     datetime = models.DateTimeField("聊天时间", default=cur_time)
#     # class Meta:
#     #     unique_together = ("a", "b")
#
from django.db import models
from utils.coder import encode_upload_image

# class A_TEST(models.Model):
#     name = models.CharField(max_length=1111)
#     img = models.ImageField(upload_to=encode_upload_image)


