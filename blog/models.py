# -*- coding: UTF-8 -*-
from django.db import models


class Tag(models.Model):
    name = models.CharField(u'名词', max_length=20)

    def __unicode__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(u'标题', max_length=50)
    subtitle = models.CharField(u'副标题', max_length=50)
    content = models.TextField(u'内容')
    summary = models.TextField(u'摘要', max_length=200, null=True)
    create_time = models.DateTimeField(u'发布时间')
    is_top = models.BooleanField(u'置顶', default=False)
    tags = models.ManyToManyField(Tag)
    status = models.BooleanField(u'状态', default=True)
    locked = models.BooleanField(u'锁定', default=False)
    month = ''
    day = ''

    def __unicode__(self):
        return self.title


class Other(models.Model):
    user_name = models.CharField(u'博主网名', max_length=10)
    motto = models.CharField(u'头像下方签名', max_length=20)
    salutatory = models.CharField(u'首页欢迎', max_length=200, null=True)


class Visitor(models.Model):
    ip = models.URLField(u'访问ip', max_length=50)
    time = models.DateTimeField(u'访问时间')








