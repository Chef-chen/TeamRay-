import json
import time
from hashlib import md5
import os
import jwt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator

from .models import User
# Create your views here.
from django.views import View
from django.conf import settings
from Tools.login_dec import login_check

class UserView(View):
    # 处理 v1/users的get请求
    def get(self, request,username=None):
        if username:
            # 返回指定用户的信息
            try:
                user = User.objects.get(username=username)
            except:
                result={'code':10104,'error':'用户名称错误！'}
                return JsonResponse(result)
            # 按格式返回
            result = {'code':200,'username':username,'data':{'avatar':str(user.avatar),'info':user.info,'pic':str(user.pic),'phone':user.phone,'email':user.email}}
            # result = {'code':200,'nickname':username,'data':{'nickname':username}}
            return JsonResponse(result)
        else:
            return HttpResponse('返回所有信息')

    # 处理 v1/users的post请求
    def post(self, request):
        # 获取前端给后端的json串
        json_str = request.body
        # 把jsson串反序列化为对象
        json_obj = json.loads(json_str)
        # 从对象【字典】中获取数据
        username = json_obj['username']
        phone = json_obj['phone']
        email = json_obj['email']
        password_1 = json_obj['password_1']
        password_2 = json_obj['password_2']
        # 数据检查
        # 注册的用户名是否可用
        old_user = User.objects.filter(username=username)
        if old_user:
            result = {'code':10100,'error':'用户名已注册'}
            return JsonResponse(result)
        # 两次密码不一致
        if password_1 != password_2:
            result = {'code':10101,'error':'两次密码不一致'}
            return JsonResponse(result)
        # 添加密码hash值
        m = md5()
        m.update(password_1.encode())
        md5_password = m.hexdigest()

        # 插入数据
        try:
            user = User.objects.create(username=username,password=md5_password,email=email,phone=phone)

        except:
            result = {'code':10102,'error':'用户名已注册'}
            return JsonResponse(result)

        # 如何记住登录状态
        token = make_token(username)
        # 将生成字节串转化为字符串
        # 新版本jwt已经自动将生成的token转化为字符串
        return JsonResponse({'code':200,'username':username,'data':{"token":token}})

    # 处理 v1/users的put请求
    @method_decorator(login_check)
    def put(self,request,username):
        # 获取前端传递的json串
        json_str = request.body
        # 将json串反序列化为对象
        json_obj = json.loads(json_str)
        # 获取要修改的用户
        user = request.myuser
        # 修改
        user.phone = json_obj['phone']
        user.email = json_obj['email']
        # 保存
        user.save()
        result = {'code':200,'username':user.username}
        return JsonResponse(result)


def make_token(username,expire=3600*24):
    key = settings.JWT_TOKEN_KEY
    now = time.time()
    payload = {'username':username,'exp':now+expire}
    # 生成token
    return jwt.encode(payload,'123456',"HS256")

@login_check
def user_avatar(request,username):
    if request.method !="POST":
        result = {'code':10105,'error':'只接受post请求'}
        return JsonResponse(result)
    # 从request中获取已经登录的用户信息
    user = request.myuser
    # 把获取到的图片存到数据库的avatar字段
    user.avatar = request.FILES['avatar']
    user.save()
    # 返回值200到前端
    result = {'code':200,'username':user.username}
    return JsonResponse(result)

@login_check
def user_pic(request,username):
    if request.method !="POST":
        result = {'code':10105,'error':'只接受post请求'}
        return JsonResponse(result)
    # 从request中获取已经登录的用户信息
    user = request.myuser
    img = request.FILES['pic']
    user.pic = img
    user.save()
    result = {'code':200,'username':user.username}
    return JsonResponse(result)

# http://127.0.0.1:8000/media/pic/1612158363(1).jpg
# http://127.0.0.1:8000/media/avatar/90e26f8f5188b0411fac3e43af1a73a.jpg

