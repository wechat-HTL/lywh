#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging

import tornado.web
import tornado.ioloop
import tornado.httpserver

from tornado.options import define, options
from logging.handlers import RotatingFileHandler

from handlers.index import IndexHandler
from handlers.novelty import *
from handlers.user import LoginHandler, LogoutHandler


formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
logger = logging.getLogger()
if options.log_file_prefix:
    logger.handlers = []
    channel = logging.handlers.TimedRotatingFileHandler(
        filename=options.log_file_prefix,
        when='midnight',
        backupCount=options.log_file_num_backups
    )
    channel.setFormatter(formatter)
    logger.addHandler(channel)


define("port", default=10080, help="run on the given port", type=int)


class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r"/", IndexHandler),

            (r"/novelty", NoveltyHandler),
            (r"/novelty/edit/([0-9Xx\-]+)", NoveltyEditHandler),
            (r"/novelty/del/([0-9Xx\-]+)", NoveltyDelHandler),
            (r"/novelty/add/([0-9Xx\-]+)", NoveltyAddHandler),
            (r"/novelty/json", NoveltyJsonHandler),
            (r"/novelty/detail/([0-9Xx\-]+)", NoveltyDetailJsonHandler),


            (r"/login", LoginHandler),
            (r"/logout", LogoutHandler),
        ]

        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "statics"),
            ui_modules=dict(
            ),
            cookie_secret='939d3d573f06c5fed9bf7',
            debug=True,
            gzip=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()

