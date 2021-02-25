from django.db import models
import uuid, os


def user_directory_pic(instance, filename):
    # return the whole path to the file
    return os.path.join(instance.username, "pic", filename)


def user_directory_avatar(instance, filename):
    # return the whole path to the file
    return os.path.join(instance.username, "avatar", filename)


# Create your models here.
class User(models.Model):
    username = models.CharField('用户名', max_length=11, unique=True)
    password = models.CharField('密码', max_length=32)
    email = models.EmailField('邮箱')
    info = models.CharField('信息', max_length=5000, null=True)
    pic = models.ImageField(upload_to=user_directory_pic, null=True)
    avatar = models.ImageField(upload_to=user_directory_avatar, null=True)
    phone = models.CharField('手机号', max_length=11)
    is_active = models.BooleanField('是否激活', default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_user_profile'
