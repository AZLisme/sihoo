# -*- coding: utf-8 -*-
"""


@author: AZLisme
@email:  helloazl@icloud.com
"""

import flask_login
from flask import g, jsonify

from sihoo.models.accounts import User


def set_title(title):
    """设定页面的标题"""
    g.title = title


def api_result(result):
    return jsonify(result=result)


def current_user() -> User:
    user = flask_login.current_user
    return user
