#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import hashlib
from handlers.basic import BasicHandler, login


class LoginHandler(BasicHandler):

    def get(self):
        self.render('login.html')                                  # 登录页面

    def post(self):
        username = self.get_argument('username', '')
        password = self.get_argument('password', '')
        remember = self.get_argument('remember', None)

        if not username or not password:
            return self.write("用户名或者密码不为空！")            # 此处可以修改成抛出一个页面
        if remember:
            remember = 30

        if self.user_ins.checkout_user_login(username, password):   # 判断用户名和密码是否匹配
            user = {
                'name': username,
                'pwd': hashlib.md5(password).hexdigest()
            }
            self.set_session(user, days=remember)
            logging.info("User login : %s" % username)
            return self.redirect("/")                               # 登录成功，重定向到主页
        return self.write("登录错误!!")                             # 此处可以修改成抛出一个页面


class LogoutHandler(BasicHandler):
    @login
    def get(self):
        self.del_session()
        self.redirect('/login')
