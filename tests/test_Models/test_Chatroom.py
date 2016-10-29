# -*- coding: utf-8 -*-
"""


@author: AZLisme
@email:  helloazl@icloud.com
"""

from nose.tools import assert_false, assert_raises

from sihoo import create_app
from sihoo.exc import SihooDatabaseNotUnique, SihooProgramException
from sihoo.models import db

app = create_app(test=True)


def setup():
    with app.app_context():
        db.create_all()


def test_create_chatroom():
    pass


def test_change_chatroom_bio():
    pass


def teardown():
    with app.app_context():
        db.metadata.drop_all(db.engine)
