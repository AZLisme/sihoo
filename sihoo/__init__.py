# -*- coding: utf-8 -*-
"""
Sihoo 包 init 模块

定义app工厂方法

@author: AZLisme
@email:  helloazl@icloud.com
"""

import flask
import tornado


def make_tornado_app():
    """创建Tornado App的工厂方法"""
    app = None
    return app


def make_flask_app():
    """创建Flask App的工厂方法"""
    app = flask.Flask('sihoo', static_folder='../front')
    app.config.from_pyfile('settings/flask-setting.py')
    from sihoo.models import db
    db.init_app(app)
    from sihoo import modules
    modules.init_app(app)
    return app
