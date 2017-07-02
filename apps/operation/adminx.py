# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/7/2 21:58'

from .models import UserAsk, CourseComment, UserFavorite, UserMessage, UserCourse

import xadmin


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']

xadmin.site.register(UserAsk, UserAskAdmin)  # register


class CourseCommentAdmin(object):
    list_display = ['user', 'course', 'comments', 'add_time']
    search_fields = ['user', 'course', 'comments']
    list_filter = ['user', 'course', 'comments', 'add_time']

xadmin.site.register(CourseComment, CourseCommentAdmin)  # register


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'course', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type', 'course']
    list_filter = ['user', 'fav_id', 'fav_type', 'course', 'add_time']

xadmin.site.register(UserFavorite, UserFavoriteAdmin)  # register


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']

xadmin.site.register(UserMessage, UserMessageAdmin)  # register


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']

xadmin.site.register(UserCourse, UserCourseAdmin)  # register