# bool => switch => BooleanField; NullBooleanField
# int => input-number => IntegerField,BigIntegerField,SmallIntegerField;
#                       PositiveBigIntegerField,BigAutoField,PositiveSmallIntegerField,SmallAutoField
#                       PositiveIntegerField,AutoField
# float => slider => FloatField,DecimalField,
# str => input => CharField; CommaSeparatedIntegerField,EmailField,SlugField,URLField,DurationField
#                 FilePathField,IPAddressField,GenericIPAddressField,TextField,BinaryField,UUIDField,JSONField,
# fk => select => RelatedField,ForeignObject,ForeignKey; OneToOneField
# m2m => multi-select => ManyToManyField,
# datetime => timepicker => DateField; DateTimeField,TimeField
# file => upload => FileField; ImageField
# other => GeneratedField
# fk_rel => ManyToOneRel; OneToOneRel,
# m2m_rel => ManyToManyRel


from django.db.models import NullBooleanField
from django.db.models import PositiveBigIntegerField,BigAutoField,PositiveSmallIntegerField,SmallAutoField,PositiveIntegerField,AutoField
from django.db.models import DecimalField,FloatField
from django.db.models import CommaSeparatedIntegerField,EmailField,SlugField,URLField,DurationField,FilePathField,IPAddressField,GenericIPAddressField,TextField,BinaryField,UUIDField,JSONField
from django.db.models import OneToOneField
from django.db.models import ManyToManyField
from django.db.models import DateTimeField,DateField,TimeField
from django.db.models import ImageField

from django.db.models import OneToOneRel
from django.db.models import ManyToManyRel


class F_bool(NullBooleanField):
    pass
class F_int(PositiveBigIntegerField,BigAutoField,PositiveSmallIntegerField,SmallAutoField,PositiveIntegerField,AutoField):
    pass
class F_float(DecimalField,FloatField):
    pass
class F_str(CommaSeparatedIntegerField,EmailField,SlugField,URLField,DurationField,FilePathField,IPAddressField,GenericIPAddressField,TextField,BinaryField,UUIDField,JSONField):
    pass
class F_fk(OneToOneField):
    pass
class F_m2m(ManyToManyField):
    pass
class F_datetime(DateTimeField):
    pass
class F_date(DateField):
    pass
class F_time(TimeField):
    pass
class F_file(ImageField):
    pass


from django.db import models
import json
def field_to_tag(model: models.Model | type, dumps=False) -> dict:
    map = {}
    obj = model() if issubclass(model, models.Model) else model
    for field in obj._meta.get_fields():
        if issubclass(F_bool, type(field)):
            map[field.name] = {'tag': 'switch', 'attrs': {}}
        elif issubclass(F_int, type(field)):
            map[field.name] = {'tag': 'input-number', 'attrs': {}}
        elif issubclass(F_float, type(field)):
            map[field.name] = {'tag': 'slider', 'attrs': {}}
        elif issubclass(F_str, type(field)):
            map[field.name] = {'tag': 'input', 'attrs': {}}
        elif issubclass(F_fk, type(field)):
            opts = field.related_model.objects.values_list('pk', flat=True).distinct()
            opts = [{'label': fk, 'value': fk} for fk in list(opts)]
            map[field.name] = {'tag': 'select-v2', 'attrs': {'multiple': False, 'opts': list(opts)}}
            # print(opts)
        elif issubclass(F_m2m, type(field)):
            opts = field.related_model.objects.values_list('pk', flat=True).distinct()
            opts = [{'label': fk, 'value': fk} for fk in list(opts)]
            map[field.name] = {'tag': 'select-v2', 'attrs': {'multiple': True, 'opts': opts}}
        elif issubclass(F_date, type(field)):
            map[field.name] = {'tag': 'date-picker', 'attrs': {'type': 'date', 'format': 'YYYY-MM-DD'}}
        elif issubclass(F_datetime, type(field)):
            map[field.name] = {'tag': 'date-picker', 'attrs': {'type': 'datetime', 'format': 'YYYY-MM-DD hh:mm:ss'}}
        elif issubclass(F_time, type(field)):
            map[field.name] = {'tag': 'time-picker', 'attrs': {}}
        elif issubclass(F_file, type(field)):
            map[field.name] = {'tag': 'upload', 'attrs': {}}
        else:
            print('未映射的被动关联字段：',type(field),field.name)
            # print(field.one_to_one)
            # print(field.one_to_many)
            # print(field.many_to_one)
            # print(field.many_to_many)

    return map if not dumps else json.dumps(map, indent=2)

from . import m_major
from ..rest import s_rest
str_to_model = {
    'auth_User': {'model': m_major.auth_User, 'serializer': s_rest.S_auth_User},
    'User': {'model': m_major.User, 'serializer': s_rest.S_User},
    'Artist': {'model': m_major.Artist, 'serializer': s_rest.S_Artist},
    'Album': {'model': m_major.Album, 'serializer': s_rest.S_Album},
    'Song': {'model': m_major.Song, 'serializer': s_rest.S_Song},
    'PlayList': {'model': m_major.PlayList, 'serializer': s_rest.S_PlayList},
    'Video': {'model': m_major.Video, 'serializer': s_rest.S_Video},
    'Image': {'model': m_major.Image, 'serializer': s_rest.S_Image},
    'Event': {'model': m_major.Event, 'serializer': s_rest.S_Event},
    'Location': {'model': m_major.Location, 'serializer': s_rest.S_Location},
    'VideoRecord': {'model': m_major.VideoRecord, 'serializer': s_rest.S_VideoRecord},
    'SongRecord': {'model': m_major.SongRecord, 'serializer': s_rest.S_SongRecord},
    'ArtistTag': {'model': m_major.ArtistTag, 'serializer': s_rest.S_ArtistTag},
    'AlbumTag': {'model': m_major.AlbumTag, 'serializer': s_rest.S_AlbumTag},
    'SongTag': {'model': m_major.SongTag, 'serializer': s_rest.S_SongTag},
    'PlayTag': {'model': m_major.PlayTag, 'serializer': s_rest.S_PlayTag},
    'VideoTag': {'model': m_major.VideoTag, 'serializer': s_rest.S_VideoTag},
    'Message': {'model': m_major.Message, 'serializer': s_rest.S_Message},
    'AlbumComment': {'model': m_major.AlbumComment, 'serializer': s_rest.S_AlbumComment},
    'SongComment': {'model': m_major.SongComment, 'serializer': s_rest.S_SongComment},
    'PlayComment': {'model': m_major.PlayComment, 'serializer': s_rest.S_PlayComment},
    'VideoComment': {'model': m_major.VideoComment, 'serializer': s_rest.S_VideoComment},
    'EventComment': {'model': m_major.EventComment, 'serializer': s_rest.S_EventComment},
}
# str_to_model_regex = ''
# for k in str_to_model.keys():
#     str_to_model_regex += f"|{k}"
# str_to_model_regex = f'({str_to_model_regex[1:]})'