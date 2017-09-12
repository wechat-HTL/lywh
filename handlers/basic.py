#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools
import tornado.web

from models.user import Users


class BasicHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(BasicHandler, self).__init__(application, request, **kwargs)
        self.user_ins = Users()

    # 存储用户的登录信息
    def set_session(self, user, days=1):
        self.set_secure_cookie("_auid", str(user['name']), expires_days=days, httponly=True)
        self.set_secure_cookie("_auth", str(user['pwd']), expires_days=days, httponly=True)

    # 删除用户session
    def del_session(self):
        self.clear_cookie("_auid")
        self.clear_cookie("_auth")

    # 重写get_current_user
    def get_current_user(self):
        username = self.get_secure_cookie('_auid')
        auth = self.get_secure_cookie('_auth')
        if username and auth:
            ret = self.user_ins.fetch_user_info_by_nickname(username)
            if auth == ret['password']:
                return username


def login(method):                              # 用户登录态控制
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):

        if not self.current_user:
            if 'Accept' in self.request.headers and self.request.headers['Accept'].find('json') >= 0:
                self.redirect('/login')
                return
            if self.request.method in ("GET", "HEAD"):
                self.redirect('/login')
                return
            self.write("验证用户错误!!")
            return
        return method(self, *args, **kwargs)
    return wrapper



