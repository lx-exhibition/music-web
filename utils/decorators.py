from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.template.response import TemplateResponse
from music.apis.v_api import HEADERS

def to_template(t_path: str, context: dict = {}):
    def view(req: HttpRequest):
        return TemplateResponse(req, t_path, context=context)
    return view

def to_text(text: str, code=200):
    def view(req: HttpRequest):
        return HttpResponse(text, content_type='text/plain', status=code, headers=HEADERS)
    return view

from confs.settings import TEMPLATES, BASE_DIR
def to_html(html: str):
    def view(req: HttpRequest):
        return HttpResponse(open(f'{BASE_DIR}/{TEMPLATES[0]["DIRS"][0]}/{html}').read(), content_type='text/html')
    return view

def to_html_raw(html: str):
    def view(req: HttpRequest):
        return HttpResponse(str, content_type='text/html')
    return view

def redirect_path(path: str):
    def view(req: HttpRequest):
        return HttpResponseRedirect(path)
    return view
