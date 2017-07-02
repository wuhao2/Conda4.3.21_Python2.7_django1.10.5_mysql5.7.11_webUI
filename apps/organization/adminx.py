# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/7/2 21:45'

from .models import City, CourseOrg, Teacher

import xadmin


class CityAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']

xadmin.site.register(City, CityAdmin)  # register


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'address', 'image', 'city', 'add_time']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums', 'address', 'image', 'city']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums', 'address', 'image', 'city', 'add_time']

xadmin.site.register(CourseOrg, CourseOrgAdmin)  # register


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums', 'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums', 'add_time']

xadmin.site.register(Teacher, TeacherAdmin)  # register