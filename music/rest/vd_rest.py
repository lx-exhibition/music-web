# rest decorators
import json

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser,MultiPartParser
from rest_framework.decorators import api_view,APIView
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from django.db.models.fields import BooleanField

from ..models.classMap import field_to_tag

# create, list
def D_CL(Model, ModelSerializer):
    def _1(func):
        # @csrf_exempt
        @api_view(['GET', 'POST'])
        def _2(req: Request, *a, **b):
            if req.method == 'GET':
                data = filter(req, Model, ModelSerializer)
                conf = field_to_tag(Model)

                return Response({'data': data, 'conf': conf})

            elif req.method == 'POST':
                data = JSONParser().parse(req)
                serializer = ModelSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return func(req,*a,*b)
        return _2
    return _1
# read, update, delete
def D_RUD(Model, ModelSerializer):
    def _1(func):
        # @csrf_exempt
        @api_view(['GET', 'PUT', 'DELETE'])
        def _2(req: Request, pk, *a, **b):

            try:
                model = Model.objects.get(pk=pk)
            except Model.DoesNotExist:
                return Response(status=404)

            if req.method == 'GET':
                serializer = ModelSerializer(model)

                conf = field_to_tag(Model)

                return Response({'data': serializer.data, 'conf': conf})

            elif req.method == 'PUT':
                data = req.data
                serializer = ModelSerializer(model, data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            elif req.method == 'DELETE':
                model.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            return func(req,pk,*a,*b)
        return _2
    return _1

def filter(req: Request, Model, ModelSerializer):
    models = Model.objects.all()

    query = req.query_params.dict()
    for f in Model()._meta.get_fields():
        if query.get(f.name) is not None:
            if isinstance(f, BooleanField):
                query[f.name] = query[f.name].lower() == 'true'
            models = models.filter(**{f.name: query.get(f.name)})

    serializer = ModelSerializer(models, many=True)
    return serializer.data


