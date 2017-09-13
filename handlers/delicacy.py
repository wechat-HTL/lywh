#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .basic import BasicHandler, login


class DelicacyHandler(BasicHandler):               # 美食页面列表

    @login
    def get(self, *args, **kwargs):
        pass


class DelicacyAddHandler(BasicHandler):               # 美食信息添加

    @login
    def post(self, *args, **kwargs):
        pass


class DelicacyEditHandler(BasicHandler):                # 美食信息编辑

    @login
    def post(self, *args, **kwargs):
        pass


class DelicacyDelHandler(BasicHandler):                   # 交通信息删除

    @login
    def post(self, *args, **kwargs):
        pass


class DelicacyJsonHandler(BasicHandler):          # 小程序调用的json接口

    def get(self, *args, **kwargs):
        pass


class DelicacyDetailJsonHandler(BasicHandler):          # 小程序单贴调用的json接口

    def get(self, *args, **kwargs):
        pass
