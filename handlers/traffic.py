#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .basic import BasicHandler, login


class TrafficHandler(BasicHandler):               # 交通页面列表

    @login
    def get(self, *args, **kwargs):
        pass


class TrafficAddHandler(BasicHandler):               # 交通信息添加

    @login
    def post(self, *args, **kwargs):
        pass


class TrafficEditHandler(BasicHandler):                # 交通信息编辑

    @login
    def post(self, *args, **kwargs):
        pass


class TrafficDelHandler(BasicHandler):                   # 交通信息删除

    @login
    def post(self, *args, **kwargs):
        pass


class TrafficJsonHandler(BasicHandler):          # 小程序调用的json接口

    def get(self, *args, **kwargs):
        pass


class TrafficDetailJsonHandler(BasicHandler):          # 小程序单贴调用的json接口

    def get(self, *args, **kwargs):
        pass
