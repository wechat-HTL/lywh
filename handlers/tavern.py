#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .basic import BasicHandler, login


class TavernHandler(BasicHandler):               # 住宿页面列表

    @login
    def get(self, *args, **kwargs):
        pass


class TavernAddHandler(BasicHandler):               # 住宿信息添加

    @login
    def post(self, *args, **kwargs):
        pass


class TavernEditHandler(BasicHandler):                # 住宿信息编辑

    @login
    def post(self, *args, **kwargs):
        pass


class TavernDelHandler(BasicHandler):                   # 住宿信息删除

    @login
    def post(self, *args, **kwargs):
        pass


class DelicacyJsonHandler(BasicHandler):          # 小程序调用的json接口

    def get(self, *args, **kwargs):
        pass


class TavernDetailJsonHandler(BasicHandler):          # 小程序单贴调用的json接口

    def get(self, *args, **kwargs):
        pass
