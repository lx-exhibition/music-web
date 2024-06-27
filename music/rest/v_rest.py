from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound,ValidationError

from ..models import m_major as m
from . import s_rest as s
MEDIA_URL = 'http://localhost:8001/media'

@api_view(['GET'])
def model_detail(req: Request, ms, pk, **kwargs):
    Model = ms['model']
    Serializer = ms['serializer']
    try:
        ret = Serializer(Model.objects.get(pk=pk)).data
    except Model.DoesNotExist:
        raise NotFound('User does not exist')
    match Model:
        case m.User:
            user = m.User.objects.get(pk=pk)
            ret['avatar'] = '{}{}'.format(MEDIA_URL, s.S_Image(user.avatar).data['data'])
            ret['location'] = s.S_Location(user.location).data
            ret['origin_user'] = s.S_auth_User(user.origin_user).data
            ret['gender'] = {0:"未知",1:"男",2:'女'}[user.gender]
            ret['birthday'] = user.birthday.strftime('%Y年%m月%d日')
            return Response(ret)
    return Response("")

