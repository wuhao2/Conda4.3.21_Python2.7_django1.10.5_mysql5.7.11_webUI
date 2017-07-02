# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/7/2 21:06'
import xadmin
from .models import Course, Lesson, Video, CourseResouce


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'studens', 'fav_nums', 'image', 'click_nums', 'add_time']  # for see all field of this class
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'studens', 'fav_nums', 'image', 'click_nums']    # for search function in Background management system.
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'studens', 'fav_nums', 'image', 'click_nums', 'add_time']  # for filter

xadmin.site.register(Course, CourseAdmin)  # register


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']  # for see all field of this class
    search_fields = ['course', 'name']    # for search function in Background management system.
    list_filter = ['course__name', 'name', 'add_time']  # for filter by foreign course name

xadmin.site.register(Lesson, LessonAdmin)  # register


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']  # for see all field of this class
    search_fields = ['lesson', 'name']    # for search function in Background management system.
    list_filter = ['lesson__name', 'name', 'add_time']  # for filter

xadmin.site.register(Video, VideoAdmin)  # register


class CourseResouceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']  # for see all field of this class
    search_fields = ['course', 'name', 'download']    # for search function in Background management system.
    list_filter = ['course__name', 'name', 'download', 'add_time']  # for filter

xadmin.site.register(CourseResouce, CourseResouceAdmin)  # register
