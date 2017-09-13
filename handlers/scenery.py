#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .basic import BasicHandler, login


class SceneryHandler(BasicHandler):               # 景点页面列表

    @login
    def get(self, *args, **kwargs):
        pass


class SceneryAddHandler(BasicHandler):               # 景点信息添加

    @login
    def post(self, *args, **kwargs):
        pass


class SceneryEditHandler(BasicHandler):                # 景点信息编辑

    @login
    def post(self, *args, **kwargs):
        pass


class SceneryDelHandler(BasicHandler):                   # 景点信息删除

    @login
    def post(self, *args, **kwargs):
        pass


class SceneryJsonHandler(BasicHandler):          # 小程序调用的json接口

    def get(self, *args, **kwargs):
        pass


class SceneryDetailJsonHandler(BasicHandler):          # 小程序单贴调用的json接口

    def get(self, *args, **kwargs):
        pass
