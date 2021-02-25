from django.db import models
from user.models import User
import uuid,os
# Create your models here.
def user_directory_pic(instance, filename):
    ext = filename.split('.')[-1]
    # return the whole path to the file
    return os.path.join(instance.username, "pic", filename)



class Topic(models.Model):
    title = models.CharField('商品名称',max_length=50)
    type = models.CharField('商品分类',max_length=20)
    limit = models.BooleanField('上架状态',default=1)
    introduce = models.CharField('信息简介',max_length=50)
    content = models.TextField('商品完整信息')
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    pic = models.ImageField(upload_to='user_directory_path',null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    # 1对多外键
    user_profile = models.ForeignKey(User,on_delete=models.CASCADE)
