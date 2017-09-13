#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .basic import BasicHandler, login


# 新鲜事
class NoveltyHandler(BasicHandler):            # 新鲜事列表查询
    """
    备注： 包含一个文章标题，主图，创建日期等
    另外缓存一个，滚动图片的列表，主要列表分页
    """
    @login
    def get(self, *args, **kwargs):
        pass


class NoveltyAddHandler(BasicHandler):          # 新鲜事创建

    @login
    def post(self, *args, **kwargs):
        pass


class NoveltyDelHandler(BasicHandler):          # 新鲜事删除

    @login
    def post(self, *args, **kwargs):
        pass


class NoveltyEditHandler(BasicHandler):          # 新鲜事编辑

    @login
    def post(self, *args, **kwargs):
        pass


class NoveltyJsonHandler(BasicHandler):          # 小程序调用的json接口

    def get(self, *args, **kwargs):
        pass


class NoveltyDetailJsonHandler(BasicHandler):          # 小程序单贴调用的json接口

    def get(self, *args, **kwargs):
        pass
