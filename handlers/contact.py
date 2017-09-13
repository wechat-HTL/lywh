#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .basic import BasicHandler, login


class ContactHandler(BasicHandler):               # 联系方式展示页面

    @login
    def get(self, *args, **kwargs):
        pass


class ContactAddHandler(BasicHandler):              # 联系方式添加页面

    @login
    def post(self, *args, **kwargs):
        pass


class ContactDelHandler(BasicHandler):                # 联系方式删除

    @login
    def post(self, *args, **kwargs):
        pass


class ContactJsonData(BasicHandler):                    # 供小程序调用数据接口

    def get(self, *args, **kwargs):
        pass
