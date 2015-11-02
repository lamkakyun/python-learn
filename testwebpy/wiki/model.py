#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
db = web.database(dbn="mysql", db='testpy', user='jet', pw="123", dburl='127.0.0.1')

def get_pages():
    return db.select('pages', order='id desc')