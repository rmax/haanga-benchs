#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a port of Haanga's benchmark suite over Tornado Framework and focuses
to be as much as possible close to PHP execution model without the overhead
of a full blown framework like Django.

Usage:
    ./hello_haanga.py
    ./hello_haanga.py --port=8000 --workers=1

By default listen on port 8888 and starts 5 workers.
"""

__author__ = "Rolando Espinoza La fuente <darkrho@gmail.com>"

import os

from datetime import datetime
from time import time

from tornado import httpserver, ioloop, template

class M_O(dict):
    """
    Makes a dictionary behaves like an object suitable for templates
    that returns None if an attribute does not exists.
    """
    def __getattr__(self, name):
        return self.get(name, '')

    def __setattr__(self, name, value):
        self[name] = value


class Application(object):
    def __init__(self, template_root):
        self.routes = {
            '/b1/': self.render_b1,
            '/b1_tpl/': self.render_b1_tpl,
            '/b2_tpl/': self.render_b2_tpl,
            '/b2_1_tpl/': self.render_b2_1_tpl,
            '/header/': self.render_header,
        }

        self.loader = template.Loader(template_root)

    def render_b1(self, request):
        s = '<p>La hora (%d) en epochs es: %d</p>'
        # calculates time() every loop
        self.finish(request, '\n'.join(s % (i, time()) for i in xrange(100)))

    def render_b1_tpl(self, request):
        def loop(i):
            # loads template and calculates time() every loop
            template = self.loader.load('b1_tpl.html')
            return template.generate(i=i, epoch=time())

        self.finish(request, ''.join(loop(i) for i in xrange(100)))

    def render_b2_tpl(self, request):
        class Foo:
            def __init__(self, i, epoch):
                self.i = i
                self.epoch = epoch

        # evaluates Foo() and time() for each loop
        objects = (Foo(i, time()) for i in xrange(100))
        template = self.loader.load('b2_tpl.html')

        self.finish(request, template.generate(objects=objects))

    def render_b2_1_tpl(self, request):
        class Foo:
            def __init__(self, i, epoch):
                # coerce to str or escape() will fail
                # because expects a string
                self.i = str(i)
                self.epoch = epoch

        # evaluates Foo() and time() for each loop
        objects = (Foo(i, datetime.today()) for i in xrange(100))
        template = self.loader.load('b2_filters_tpl.html')

        # Haanga uses native php's date function
        # we will use strftime which is already available
        # in the template with the datetime module
        # We pass RFC 2822 compatible date format to emulate php's r format
        date_format = '%a, %d %b %Y %H:%M:%S +0000'
        self.finish(request, template.generate(objects=objects,
                                               date_format=date_format))

    def render_header(self, request):
        title = "Cabecera menéame"
        globals = {}
        globals['favicon'] = "icon.jpg"
        globals['noindex'] = True
        globals['tags'] = 'test1, test2'
        globals['description'] = 'Pruebas de descripción'
        globals['server_name'] = 'www.meneame.net'
        globals['base_url'] = '/'


        globals['base_static'] = 'http://static.meneame.net'
        globals['js_main'] = 'general01.php'
        globals['security_key'] = 'xxxxxxxxxxxxxxxxxxxxxxx'


        globals['thumbnail'] = 'void.jpg'
        globals['thumbnail_logo'] = 'void.jpg'
        globals['extra_head'] = ''
        globals['extra_js'] = ('void.js', 'void1.js')
        globals['q'] = 'q=aslkdlñak ñlsakd ñlaks&kasjlkadjlajsdljkl'
        globals['lang'] = 'es'
        globals['css_main'] = 'main.css'
        globals['css_color'] = 'main.css'

        template = self.loader.load('header.html')
        context = {
            'title': title,
            # wrap global into dict-with-attr-access object
            # workaround meneame's we-like-to-access-undefined-variables-in-templates
            'globals': M_O(globals),
            'current_user': None,
        }

        parts = []
        parts.append(template.generate(**context))
        parts.append(template.generate(**context))
        parts.append(template.generate(**context))

        self.finish(request, ''.join(parts))

    def notfound(self, request):
        request.write("HTTP/1.1 404 NotFound\r\nContent-Length: 0\r\n\r\n")
        request.finish()

    def finish(self, request, content):
        request.write("HTTP/1.1 200 OK\r\nContent-Length: %d\r\n\r\n%s" % \
                      (len(content), content))
        request.finish()

    def __call__(self, request):
        self.routes.get(request.uri, self.notfound)(request)

def main():
    from tornado.options import define, options, parse_command_line

    define('port', default=8888, help="Run on given ports (default: 8888)", type=int)
    define('workers', default=5, help="Number of workers (default: 5)", type=int)

    parse_command_line()

    template_root = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates')
    app = Application(template_root)

    http_server = httpserver.HTTPServer(app)
    http_server.bind(options.port)
    http_server.start(options.workers)

    print "Listening at: http://127.0.0.1:%d/" % options.port
    ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
