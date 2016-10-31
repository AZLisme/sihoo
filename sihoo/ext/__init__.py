# -*- coding: utf-8 -*-
"""
Sihoo 扩展模块

@author: AZLisme
@email:  helloazl@icloud.com
"""
from sihoo.ext import login, socketio


def configure(app):
    login.configure(app)
    socketio.configure(app)
