from django.urls import path

from .vd_rest import D_CL,D_RUD

def _(req, format=None):
    pass

from rest_framework.response import Response
from rest_framework.decorators import api_view
def cl(req, model):
    return D_CL(model['model'], model['serializer'])(_)(req)
def rud(req, model, pk):
    return D_RUD(model['model'], model['serializer'])(_)(req,pk)
@api_view(['GET'])
def ids(req, model):
    Model = model['model']
    ids = Model.objects.values_list('pk', flat=True).distinct()
    ids = [{'label': fk, 'value': fk} for fk in list(ids)]
    print(ids)
    return Response(ids)
@api_view(['GET'])
def cols(req, model):
    Model = model['model']
    cols = Model()._meta.get_fields()
    cols = [v.name for v in cols]
    return Response(cols)

@api_view(['GET'])
def model_types(req):
    return Response([k for k in str_to_model])

# ---------------------- 路由

from django.urls import register_converter
from ..models.classMap import str_to_model
def list_to_regex(lst: list):
    res = ''
    for s in lst:
        res += f'|{s}'
    return f'({res[1:]})'
# 路径映射(PathMapping) => 模型
class PM_model:
    regex = list_to_regex(str_to_model.keys())
    def to_python(self, value):
        # print(value)
        return str_to_model[value]
    def to_url(self, value):
        return value
register_converter(PM_model, "model")

from .v_utils import UTILS
class PM_utils:
    regex = list_to_regex(UTILS)
    def to_python(self, val):
        return val
    def to_url(self, val):
        return val
register_converter(PM_utils, 'utils')

# ---------------------- api 文档

from rest_framework.reverse import reverse
@api_view(['GET'])
def index(req,format=None):
    res = Response({
        'index': reverse('index', request=req,format=format),
        **{
            f'{k}-cl': reverse('model-cl', kwargs={'model': k}, request=req,format=format)
            for k in str_to_model.keys()
        },
        **{
            f'{k}-ids': reverse('model-ids', kwargs={'model': k}, request=req,format=format)
            for k in str_to_model.keys()
        },
        **{
            f'{k}-cols': reverse('model-cols', kwargs={'model': k}, request=req,format=format)
            for k in str_to_model.keys()
        },
        'model-types': reverse('model-types', request=req,format=format),

        **{
            f'utils-{v}': reverse('utils', kwargs={'util': v}, request=req,format=format)
            for v in UTILS
        },
    })
    # res.accepted_renderer = JSONRenderer()
    # res.accepted_media_type = 'application/json'
    # res.renderer_context = {}
    return res

from . import v_rest,v_utils
urlpatterns =[
    path('', index, name='index'),
    path('<model:model>/', cl, name='model-cl'),
    path('<model:model>/<int:pk>/', rud, name='model-rud'),
    path('<model:ms>/<int:pk>/d/', v_rest.model_detail, name='model-detail'),
    path('<model:model>/ids/', ids, name='model-ids'),
    path('<model:model>/cols/', cols, name='model-cols'),
    path('model-types/', model_types, name='model-types'),
]
urlpatterns+=[
    path('<utils:util>/', v_utils.V_utils, name='utils'),
]

from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = format_suffix_patterns(urlpatterns)
