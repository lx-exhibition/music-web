import json

from django.utils.deprecation import MiddlewareMixin
from django.http import HttpRequest, HttpResponse
from .apis.v_api import RES_NOT_AUTH
from django.contrib.sessions.models import Session

HEADERS = {
    'Access-Control-Allow-Origin': 'http://localhost:5173',
    # 'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': "Content-Type,XFILENAME,XFILECATEGORY,XFILESIZE",
    'Access-Control-Allow-Methods': "GET,PUT,POST,DELETE,OPTIONS,TRACE,PATCH,HEAD",
    'Access-Control-Allow-Credentials': 'true',
}

class LoginRequiredMiddleware(MiddlewareMixin):
    def process_request(self, req: HttpRequest):
        # print(json.dumps(dict(req.headers), indent=2))
        # print(req.session.items())
        # print(req.COOKIES)
        pass

    def process_response(self, req: HttpRequest,res: HttpResponse):
        # print(req.COOKIES)
        # print(req.COOKIES.items())
        # print(req.session)
        # print(req.session.items())
        # req.session['test1'] = 123
        # req.session.set_expiry(10)
        # res.set_signed_cookie('test','test',0)
        # res.set_signed_cookie('test','hello','weowihr')
        # res.delete_cookie('test')

        print(req.META.get('HTTP_ORIGIN'))
        # res.headers['Access-Control-Allow-Origin'] = '*'
        res.headers['Access-Control-Allow-Origin'] = req.META.get('HTTP_ORIGIN')
        res.headers['Access-Control-Allow-Headers'] = 'Content-Type,XFILENAME,XFILECATEGORY,XFILESIZE,X-CSRFTOKEN'
        res.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS,TRACE,PATCH,HEAD'
        res.headers['Access-Control-Allow-Credentials'] = 'true'
        # print(json.dumps(dict(req.headers), indent=2))
        return res

