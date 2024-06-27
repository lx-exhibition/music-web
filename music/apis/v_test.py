import json
import math
import random
from pathlib import Path
from django.http import HttpRequest,HttpResponse,JsonResponse
HEADERS = {
    'Access-Control-Allow-Origin': 'http://localhost:5173',
    'Access-Control-Allow-Headers': "Content-Type,XFILENAME,XFILECATEGORY,XFILESIZE"
}
dir = 'E:/g/12.天使☆騒々RE-BOOT!/[ゆずソフト] 天使☆騒々 RE-BOOT! [JPG]'

def RES_OK(obj=None, code=200):
    return JsonResponse({'data': obj, 'code': code}, status=code, headers=HEADERS)


def img(req: HttpRequest, path):
    print(req.headers.get('Content-Type'))
    if req.method == 'OPTIONS':
        return RES_OK()

    if path == '':
        path = Path(dir)
        files = [file.name for file in path.glob('*.*')]
        print(files[:10])
        return HttpResponse(json.dumps(files),content_type='text/plain',headers={'Access-Control-Allow-Origin': '*'})

    print(path)
    with open(f'{dir}/{path}','rb') as f:
        print(f)
        return HttpResponse(f.read(), content_type='image/jpeg',headers=HEADERS)

from .v_api import RES_FORBID
from .utils import send_msg
from django.core.cache import caches
def send_mail(req: HttpRequest):
    token = math.floor(random.random()*10000)
    token = '{:0<4d}'.format(token)

    mail = req.GET.get('email')
    if not mail:
        return RES_FORBID('邮箱不能为空')

    try:
        send_msg('邮箱认证', token, mail)
    except Exception as e:
        return RES_FORBID('邮箱发送失败')

    username = req.GET.get('username')
    salt = math.floor(random.random()*1000000000)
    key = f'email_token${username}${salt}'
    caches['my_cache'].set(key, token)

    return HttpResponse(key, headers=HEADERS)
