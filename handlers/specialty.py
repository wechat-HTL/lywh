#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .basic import BasicHandler, login


class SpecialtyHandler(BasicHandler):               # 特产页面列表

    @login
    def get(self, *args, **kwargs):
        pass


class SpecialtyAddHandler(BasicHandler):               # 特产信息添加

    @login
    def post(self, *args, **kwargs):
        pass


class SpecialtyEditHandler(BasicHandler):                # 特产信息编辑

    @login
    def post(self, *args, **kwargs):
        pass


class SpecialtyDelHandler(BasicHandler):                   # 特产信息删除

    @login
    def post(self, *args, **kwargs):
        pass


class SpecialtyJsonHandler(BasicHandler):          # 小程序调用的json接口

    def get(self, *args, **kwargs):
        pass


class SpecialtyDetailJsonHandler(BasicHandler):          # 小程序单贴调用的json接口

    def get(self, *args, **kwargs):
        pass
