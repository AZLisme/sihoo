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


def make_flask_app(config=None, test=False):
    """创建Flask App的工厂方法

    # 配置文件读取流程

    1. 首先从 settings/flask-setting.py 中读取默认配置
    2. 然后从环境变量 SIHOO_SETTINGS 中尝试读取服务器内独立配置文件
    3. 最后从参数中读取配置

    配置项目的优先级从低到高，依次覆盖

    如果是处在测试环境，则同样的流程，只是相关文件与变量替换为：flask-setting-test 与 SIHOO_TEST_SETTINGS
    """
    app = flask.Flask('sihoo', static_folder='../front')
    if test:
        app.testing = True
        app.config.from_pyfile('settings/flask-setting-test.py')
        app.config.from_envvar('SIHOO_TEST_SETTINGS', silent=True)
    else:
        app.config.from_pyfile('settings/flask-setting.py')
        app.config.from_envvar('SIHOO_SETTINGS', silent=True)
    if config:
        app.config.update(config)
    from sihoo.models import db
    db.init_app(app)
    from sihoo import modules
    modules.init_app(app)
    return app
