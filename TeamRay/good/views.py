from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View

from Tools.login_dec import login_check
import json,os

from good.models import Topic
from user.models import User


class GoodView(View):
    @method_decorator(login_check)
    def post(self, request, user_id):
        # 1 从请求对象的附加数据中获取用户对象
        author = request.myuser
        # 2 从前端获取用户输入的值(内容,不带格式的内容,权限的值)
        json_str = request.body
        json_obj = json.loads(json_str)
        content = json_obj['content']
        type = json_obj['type']
        price = json_obj['price']
        pic = json_obj['pic']
        print('这是商品的价格' + price)
        title = json_obj['title']
        # 3 检查分类的值一定是tec 或no-tec
        if type not in ['车源', '房源']:
            result = {'code': 10300, 'error': '类别错误'}
            return JsonResponse(result)
        # 5.数据入库
        user = User.objects.get(username=user_id)
        Topic.objects.create(title=title, content=content, type=type,
                             price=price, user_profile_id=user.id,pic=pic)
        # 6 返回
        return JsonResponse({'code': 200})

    def get(self, request, user_id=None):
        if user_id:
            # 返回指定用户的信息
            try:
                user = User.objects.get(username=user_id)
                good_list = user.topic_set.all()
                i = 0
                good_dic_list = []
                for good in good_list:
                    good_dic = {}
                    i += 1
                    good_dic[f'title'] = good.title
                    good_dic[f'price'] = good.price
                    good_dic[f'content'] = good.content
                    good_dic[f'pic']=str(good.pic)
                    good_dic_list.append(good_dic)
                print(good_dic_list)
            except:
                result = {'code': 10104, 'error': '用户名!!!!!!!!称错误！'}
                return JsonResponse(result)
            # 按格式返回
            result = {'code': 200, 'username': user_id,
                      'data': {'avatar': str(user.avatar),
                               'info': user.info, 'pic': str(user.pic),
                               'phone': user.phone, 'email': user.email},
                                'good_data_list':good_dic_list,}
            return JsonResponse(result)
        else:
            return HttpResponse('返回所有信息')


def Good_list(request,good_name):
    print('收到',good_name)
    goods_list = Topic.objects.filter(title__contains=f'{good_name}')

    if good_name in {'','*','123'}:
        goods_list = Topic.objects.all()
    good_data = []
    for good in goods_list:
        good_dic={}
        good_dic['title']=good.title
        good_dic['price']=good.price
        good_dic['type']=good.type
        good_dic['pic']=str(good.pic)
        good_dic['content']=good.content
        good_dic['time']=str(good.created_time)[0:4]
        good_dic['user']=good.user_profile.username
        good_data.append(good_dic)
    if good_data:
        result = {'code':200,'data':good_data}
        print('已成功返回')
    else:
        result = {'code': 201, 'data': '无此类商品'}
        print('已失败返回')

    return JsonResponse(result)