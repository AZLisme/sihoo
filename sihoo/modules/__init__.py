# -*- coding: utf-8 -*-
"""
Modules 文件夹用于放置按功能区分的视图脚本。相当于MVC中的Controller。

@author: AZLisme
@email:  helloazl@icloud.com
"""

from flask import Flask

def init_app(app: Flask):
    # 依次注册蓝图
    from sihoo.modules import accounts, index
    app.register_blueprint(accounts.blue_print)
    app.register_blueprint(index.blue_print)
