# -*- coding: utf-8 -*-
"""


@author: AZLisme
@email:  helloazl@icloud.com
"""

from flask_login import LoginManager

from sihoo.models.accounts import User

login_manager = LoginManager()


@login_manager.user_loader
def load_user(uid):
    return User.with_id(uid)


def configure(app):
    login_manager.init_app(app)
