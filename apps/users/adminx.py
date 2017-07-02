# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/7/2 20:06'
# Register your models into django Background management system.

import xadmin
from .models import EmailVerifyRecord, Banner


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']  # for see all field of this class
    search_fields = ['code', 'email', 'send_type']    # for search function in Background management system.
    list_filter = ['code', 'email', 'send_type', 'send_time']  # for filter

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)  # register


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']  # for see all field of this class
    search_fields = ['title', 'image', 'url', 'index']    # for search function in Background management system.
    list_filter = ['title', 'image', 'url', 'index', 'add_time']  # for filter

xadmin.site.register(Banner, BannerAdmin)  # register
