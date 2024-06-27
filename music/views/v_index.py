import datetime
import json
import time

import requests
from django.core.files.uploadedfile import TemporaryUploadedFile
from django.http import HttpRequest, HttpResponse, FileResponse
from django.template.response import TemplateResponse
from django.contrib.auth.models import User as auth_User


def index(req: HttpRequest):
    # auth_User.objects.create_user(username="真栗栗", password="123", is_staff=True)

    return HttpResponse("hello world")

def test(req: HttpRequest):
    match req.method:
        case 'GET':

            return HttpResponse("gu")
        case 'POST':
            return HttpResponse("index-test: 歌曲创建成功")
        case _:
            return HttpResponse("index-test: 请求方法错误")



from ..models.m_major import *
from django.core.files import File
from io import BytesIO

def init_artist():
    url = "http://p2.music.126.net"
    f = open("data/artist.json", 'r', encoding="utf-8")
    for x in json.loads(f.read()):
        print(x['nickname'])
        u = auth_User.objects.create_user(username=x['nickname'], password="123", is_staff=True)
        avatar = Image.objects.create()
        avatar.data.save(f'{x['nickname']}${x['stagename']}$avatar.jpg',
                         File(BytesIO(requests.get(f'{url}/{x["avatar_url"]}').content)))
        back = Image.objects.create()
        avatar.data.save(f'{x['nickname']}${x['stagename']}background.jpg',
                         File(BytesIO(requests.get(f'{url}/{x["back_url"]}').content)))
        a = User.objects.create(nickname=x['nickname'], origin_user=u, avatar=avatar)
        a.save()
        aa = Artist.objects.create(account=a, stagename=x['stagename'], description=x['desc'], background=back)
        aa.save()

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def upload(req: HttpRequest):
    print(req.headers)
    if req.method == 'OPTIONS':
        return HttpResponse(headers={'Access-Control-Allow-Origin': '*'})


    # print(req.method)
    # print(req.POST)
    print(type(req.FILES))
    print(type(req.FILES['file']))
    with open(f'upload/{time.time()}.jpg','wb') as f:
        ff = req.FILES['file']
        f.write(ff.read())
    return HttpResponse("status=200",headers={'Access-Control-Allow-Origin': '*'})

# def h(f: TemporaryUploadedFile):

from pathlib import Path
dir = 'E:/g/12.天使☆騒々RE-BOOT!/[ゆずソフト] 天使☆騒々 RE-BOOT! [JPG]'

def img(req: HttpRequest,path):
    if path == '':
        if req.method == 'OPTIONS':
            return HttpResponse(headers={'Access-Control-Allow-Origin': '*'})
        else:
            path = Path(dir)
            files = [file.name for file in path.glob('*.*')]
            print(files[:10])
            return HttpResponse(json.dumps(files),content_type='text/plain',headers={'Access-Control-Allow-Origin': '*'})

    print(path)
    with open(f'{dir}/{path}','rb') as f:
        print(f)
        return HttpResponse(f.read(), content_type='image/jpeg')

