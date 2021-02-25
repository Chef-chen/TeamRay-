from celery import Celery
from django.conf import settings
import os

# 1 添加环境变量告诉celery为哪一个django对象提供服务(从manage里第一行复制)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TeamRay.settings')

# 2 创建对象
app = Celery('TeamRay')

# 3 配置celery
app.conf.update(BROKEN_URL='redis://@127.0.0.1:6379/1',)

# 4 告知celery 自动到Django项目的应用下查找任务函数
app.autodiscover_tasks(settings.INSTALLED_APPS)

