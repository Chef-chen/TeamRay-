# Generated by Django 2.2.12 on 2021-02-22 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0003_user_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='商品名称')),
                ('type', models.CharField(max_length=20, verbose_name='商品分类')),
                ('limit', models.CharField(max_length=20, verbose_name='上架状态')),
                ('introduce', models.CharField(max_length=50, verbose_name='信息简介')),
                ('content', models.TextField(verbose_name='商品完整信息')),
                ('pic', models.ImageField(null=True, upload_to='pic')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
    ]
