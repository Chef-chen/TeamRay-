from django.http import JsonResponse
import jwt
from user.models import User

def login_check(func):
    def wrap(request, *args, **kwargs):
        # 在请求中获取前端提交过来的token
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            result = {'code': 403, 'error': '请登录！'}
            return JsonResponse(result)
        try:
            payload = jwt.decode(token,'123456','HS256')
        except:
            result = {'code': 403, 'error': '请登录！'}
            return JsonResponse(result)

        username = payload['username']
        user = User.objects.get(username=username)

        request.myuser = user

        return func(request, *args, **kwargs)

    return wrap
