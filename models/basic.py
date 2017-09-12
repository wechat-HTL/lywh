#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db_manage import global_mysql


class Basic(object):
    def __init__(self):
        super(Basic, self).__init__()
        self.g_mysql = global_mysql                    # 导入mysql连接

    def insert_info_to_mysql(self, sql):            # mysql 数据插入操作
        return self.g_mysql.insert(sql)

