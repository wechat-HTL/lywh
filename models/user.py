#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib

from models.basic import Basic


class Users(Basic):
    def __init__(self):
        super(Users, self).__init__()

    def checkout_user_login(self, nickname, pwd):                       # 用户登录查询
        sql = "select id, password from users where nickname='%s'" % nickname
        ret = self.g_mysql.get(sql)
        if not ret:
            return False
        if hashlib.md5(pwd).hexdigest() != ret['password']:
            return False
        return True

    def update_user_pwd(self, nickname, pwd):                             # 更新用户信息
        sql = "update users set password='%s' where nickname='%s'" % (pwd, nickname)
        self.g_mysql.execute(sql)

    def fetch_user_info_by_nickname(self, nickname):                     # 获取用户信息
        sql = "select * from users " \
              "where nickname='%s'" % nickname
        return self.g_mysql.get(sql)
