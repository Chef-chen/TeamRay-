import json
from hashlib import md5

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from user.models import User
from user.views import make_token


class TokenView(View):
    def get(self, request):
        pass

    def post(self, request):
        # 获取前端传递的json串
        json_str = request.body
        # 将json串序列化为对象
        json_obj = json.loads(json_str)
        # 获取数据
        username = json_obj['username']
        password = json_obj['password']

        # 校验
        try:
            user = User.objects.get(username=username)
        except:
            result = {'code':10200,'error':'用户名或密码错误！'}
            return JsonResponse(result)
        # 计算密码的hash
        m = md5()
        m.update(password.encode())
        password_h = m.hexdigest()

        #与数据库中的密码hash对比
        if password_h!=user.password:
            result = {'code':10201,'error':'用户名或密码错误！'}
            return JsonResponse(result)

        # 签发token
        token = make_token(username)

        return JsonResponse({'code':200,'username':username,'data':{"token":token}})

