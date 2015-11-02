#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import markdown # sudo pip install markdown
from web.contrib.template import render_jinja

urls = (
    '/', 'Index',
    '/new', 'New',
    '/delete/(\d+)', 'Delete',
    '(.*)', 'Page'
)

t_globals = dict(
    datestr = web.datestr,
    markdown = markdown.markdown
)

# render = render_jinja(
#     'templates',
#     encoding = 'utf-8'
# )

render = web.template.render('templates')


class Index:
    def GET(self):
        db = web.database(dbn="mysql", db='testpy', user='jet', pw="123", dburl='127.0.0.1')
        pages = db.select('pages', order='id desc')
        # return pages
        return render.index(pages)


if __name__ == '__main__':
    app = web.application(urls, globals())
    web.wsgi.runwsgi = lambda func, addr = None: web.wsgi.runfcgi(func, addr)
    app.run()