import json

from django.http import HttpRequest, JsonResponse, HttpResponse, QueryDict
from django.views.decorators.http import require_http_methods,require_POST,require_GET,require_safe

# ========= 跨域请求
HEADERS = {
    'Access-Control-Allow-Origin': 'http://localhost:5173',
    'Access-Control-Allow-Headers': "Content-Type,XFILENAME,XFILECATEGORY,XFILESIZE",
    'Access-Control-Allow-Methods': "GET,PUT,POST,DELETE,OPTIONS,TRACE,PATCH,HEAD",
    'Access-Control-Allow-Credentials': 'true',
}

# ========== 语义化响应
def MY_RESPONSE(data, code=200):
    return JsonResponse({'data': data, 'code': code}, status=code, headers=HEADERS)
def RES_CREATED(data=None, code=201):
    return MY_RESPONSE(data, code)
def RES_OK(data=None, code=200):
    return MY_RESPONSE(data, code)
def RES_READED(data=None, code=200):
    return MY_RESPONSE(data, code)
def RES_UPDATED(data=None, code=200):
    return MY_RESPONSE(data, code)
def RES_DELETED(data=None, code=204):
    return MY_RESPONSE(data, code)
def RES_BAD_REQ(err='', code=400):
    return MY_RESPONSE({'msg': f'[error] {err}'}, code)
def RES_NOT_AUTH(err='', code=401):
    return MY_RESPONSE({'msg': f'[error] {err}'}, code)
def RES_FORBID(err='', code=403):
    return MY_RESPONSE({'msg': f'[error] {err}'}, code)
def NOTFOUND(req: HttpRequest):
    return MY_RESPONSE({'msg': f'[error] api not founded'}, 404)

# ========== crud 便捷函数
def CREATE(Model, dict_, dict_f=None):
    model = Model()
    for field in model._meta.get_fields():
        # print(field)  # 模型的字段实例
        # print(type(field))
        if field.name in dict_:
            setattr(model, field.name, dict_[field.name])
        if dict_f is not None and field.name in dict_f:
            setattr(model, field.name, dict_f[field.name])
    model.save()
    return model
def READ(Model, pk):
    return Model.objects.get(pk=pk)
def UPDATE(Model, pk, dict_):
    model = Model.objects.get(pk=pk)
    for field in model._meta.get_fields():
        if field.name in dict_:
            print(field.name)
            if isinstance(field, models.ManyToManyField):
                print(f'{field.name} is many-to-many field')
                print(field)
                print(type(field))
                setattr(model, field.name, dict_[field.name])
            else:
                setattr(model, field.name, dict_[field.name])
    model.save()
    return model
def DELETE(Model, pk):
    Model.objects.filter(pk=pk).delete()


# ========== 模型编码器，参见 https://docs.djangoproject.com/zh-hans/5.0/topics/serialization/
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.core.serializers import serialize, deserialize
class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, models.FileField):
            return str(obj)
        return super().default(obj)
def JSON_SERIALIZE(model: models.Model):
    ret = serialize('json', [model,], cls=LazyEncoder)
    return json.loads(ret)[0]
def JSON_SERIALIZE_ALL(models: [models.Model]):
    ret = serialize('json', models, cls=LazyEncoder)
    return json.loads(ret)


# 视图过滤器 => 提供 CRUD 请求的处理
# 注：read / update / delete 必须提供 id
# 注2：read 不支持读取包含文件字段的模型
# @param Model => 需要处理 CRUD 的模型类
# @param code => 指定需要的过滤器，如  1010 表示只需要 create 和 update 的过滤器
POST_CONTENT_TYPE = ['multipart/form-data', 'application/x-www-form-urlencoded']
REQUIRED_CONTENT_TYPE = ['application/json', None, '']
def FILTER_CRUD(Model, code='1111'):
    def _1(func):
        def _2(req: HttpRequest, *a, **b):
            content_type = req.content_type
            print(f'Content-Type: "{content_type}"')

            if req.method == 'OPTIONS':
                return RES_OK()

            if code[0] == '1' and content_type in POST_CONTENT_TYPE:
                if req.method == 'POST':
                    model = CREATE(Model, req.POST, req.FILES)
                    return RES_CREATED(JSON_SERIALIZE(model))

            id = req.GET.get('id')

            if content_type in [*POST_CONTENT_TYPE, *REQUIRED_CONTENT_TYPE]:
                if code[1] == '1' and req.method == 'GET':
                    if req.GET.get('all') == 'true':
                        models = Model.objects.all()
                        return RES_READED(JSON_SERIALIZE_ALL(models))
                    else:
                        try:
                            model= Model.objects.get(pk=id)
                            return RES_READED(JSON_SERIALIZE(model))
                        except Model.DoesNotExist:
                            return RES_BAD_REQ(f'查询不到 id 为 {id} 的 {Model} 对象')
                if code[2] == '1' and req.method == 'PUT':
                    try:
                        data = QueryDict(req.body).get('data')
                        data = json.loads(data)
                        # Model.objects.filter(pk=data['pk']).update(**data['fields'])

                        s = JSON_SERIALIZE_ALL(Model.objects.filter(pk=data['pk']))
                        for obj,d in deserialize('json',s):
                            print(obj)

                        # print(data)
                        # print(type(data))
                        # ret = deserialize('json', [data,])
                        # for v in deserialize('json', [data,]):
                        #     print(123)

                        # for v in ret:
                        #     print(v.object)

                        # model = UPDATE(Model, data['pk'], data)
                        return RES_UPDATED(data)
                    except Model.DoesNotExist:
                        return RES_BAD_REQ(f'不存在 id 为 {id} 的 {Model} 对象')
                if code[3] == '1' and req.method == 'DELETE':
                    try:
                        DELETE(Model, id)
                        return RES_DELETED()
                    except Model.DoesNotExist:
                        return RES_BAD_REQ(f'不存在 id 为 {id} 的 {Model} 对象')
            return func(req, *a, **b)
        return _2
    return _1
def NOT_FILTED():
    return RES_BAD_REQ('访问失败，请检查 http method 是否合适，或者检查 Content-Type 头是否配置正确')


from django.contrib.auth import authenticate
from django.contrib.auth.models import User as auth_User
from django.core.cache import caches

# POST => create
# GET => read
# PUT => update
# DELETE => delete
@FILTER_CRUD(auth_User, code='0111')
def crud_AuthUser(req: HttpRequest):
    print(req.headers.get('Content-Type'))
    print(req.COOKIES)


    if req.method == 'POST':

        username = req.POST.get('username')
        password = req.POST.get('password')
        email = req.POST.get("email")
        token = req.POST.get("token")
        key = req.GET.get("key")
        token_confirm = caches['my_cache'].get(key)

        if token_confirm is None:
            return RES_FORBID('请先发送邮箱进行验证')

        print(key)
        print(token)
        print(token_confirm)

        if token != token_confirm:
            return RES_FORBID('验证码错误')

        try:
            auth_User.objects.get(username=username)
            return RES_FORBID('用户名已被注册')
        except auth_User.DoesNotExist:
            user = auth_User.objects.create_user(username=username, password=password, email=email)
            return RES_CREATED(JSON_SERIALIZE(user))




from ..models.m_major import User,Artist,Album,Song,PlayList,Video,Image,Event,Location
from ..models.mf_major import SongRecord,VideoRecord,ArtistTag,AlbumTag,SongTag,PlayTag,VideoTag
@FILTER_CRUD(User)
def crud_user(req: HttpRequest):
    return NOT_FILTED()
@FILTER_CRUD(Artist)
def crud_Artist(req: HttpRequest):
    return NOT_FILTED()
@FILTER_CRUD(Album)
def crud_Album(req: HttpRequest):
    return NOT_FILTED()
@FILTER_CRUD(Song)
def crud_Song(req: HttpRequest):
    return NOT_FILTED()
@FILTER_CRUD(PlayList)
def crud_PlayList(req: HttpRequest):
    return NOT_FILTED()
@FILTER_CRUD(Video)
def crud_Video(req: HttpRequest):
    return NOT_FILTED()
@FILTER_CRUD(Image)
def crud_Image(req: HttpRequest):
    return NOT_FILTED()
@FILTER_CRUD(Event)
def crud_Event(req: HttpRequest):
    return NOT_FILTED()
@FILTER_CRUD(Location)
def crud_Location(req: HttpRequest):
    return NOT_FILTED()
@FILTER_CRUD(SongRecord)
def crud_SongRecord(req: HttpRequest):
    return NOT_FILTED()
@FILTER_CRUD(VideoRecord)
def crud_VideoRecord(req: HttpRequest):
    return NOT_FILTED()
@FILTER_CRUD(ArtistTag)
def crud_ArtistTag(req: HttpRequest):
    return NOT_FILTED()
@FILTER_CRUD(AlbumTag)
def crud_AlbumTag(req: HttpRequest):
    return NOT_FILTED()
@FILTER_CRUD(SongTag)
def crud_SongTag(req: HttpRequest):
    return NOT_FILTED()
@FILTER_CRUD(PlayTag)
def crud_PlayTag(req: HttpRequest):
    return NOT_FILTED()
@FILTER_CRUD(VideoTag)
def crud_VideoTag(req: HttpRequest):
    return NOT_FILTED()


from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.contrib.auth import authenticate,login
from ..models.m_index import A_TEST
@FILTER_CRUD(A_TEST)
def crud_TEST(req: HttpRequest):
    # authenticate(username=)

    # print(req.COOKIES)
    # jr = RES_OK('你就是歌姬吧')
    # jr.set_cookie('test', 'jiba', max_age=3600)
    # return jr

    # req.session.sa = True
    # print(req.session.get('test'))
    # req.session.set_expiry(1000)
    return NOT_FILTED()


