#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .basic import BasicHandler, login


# 首页
class IndexHandler(BasicHandler):

    @login
    def get(self):                                  # 页面统计信息，相当于概况页面（也可以在改页面创建新的用户）
        pass

    @login
    def post(self):                                 # admin 创建新用户post动作
        pass
