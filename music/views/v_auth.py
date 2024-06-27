from django.http import HttpRequest, HttpResponse
from django.template.response import TemplateResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, UserManager
from django.contrib.auth.decorators import login_required, permission_required


def _login(req: HttpRequest):
    match req.method:
        case 'GET':
            return TemplateResponse(req,"auth/login.html")
        case 'POST':
            username = req.POST['username']
            password = req.POST['password']
            user = authenticate(req, username=username, password=password)
            if user is not None:
                login(req, user)
                return HttpResponse(f"auth-login: 登录成功, {user}")
            else:
                return HttpResponse("auth-login: 登录失败，用户不存在或密码错误")
        case _:
            return HttpResponse("auth-login: 请求方法错误")

def _register(req: HttpRequest):
    match req.method:
        case 'GET':
            return TemplateResponse(req,"auth/register.html")
        case 'POST':
            username = req.POST['username']
            password = req.POST['password']
            email = req.POST['email']
            user = authenticate(req, username=username, password=password, email=email)
            if user is not None:
                return HttpResponse("auth-register: 注册失败，可能用户名已被注册")
            else:
                User.objects.create_user(username=username, password=password, email=email)
                return HttpResponse("auth-register: 注册成功")
        case _:
            return HttpResponse("auth-register: 请求方法错误")

def _logout(req: HttpRequest):
    logout(req)
    return HttpResponse("auth-logout: 登出成功")



