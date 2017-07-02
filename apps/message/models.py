# _*_ coding=utf-8 _*_
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserMessage(models.Model):
    object_id = models.CharField(max_length=50, default='', primary_key=True, verbose_name=u"主键")
    name = models.CharField(max_length=20, null=True, blank=True, default="", verbose_name=u"用户名")
    email = models.EmailField(verbose_name=u"邮箱")
    address = models.CharField(max_length=100, verbose_name=u"联系地址")
    message = models.CharField(max_length=500, verbose_name=u"留言信息")

    class Meta:
        verbose_name=u"留言信息"
        verbose_name_plural = verbose_name
    # db_table = "user_message" # Specifies the name of the generated table by self
    # ordering = "-object_id"   # reverse order according by object_id

# defined field in models
# models.ForeignKey
# models.DateField
# models.IntegerField
# models.IPAddressField
# models.ImageField
# models.FileField
