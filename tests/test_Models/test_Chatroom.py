# -*- coding: utf-8 -*-
"""


@author: AZLisme
@email:  helloazl@icloud.com
"""

from nose.tools import assert_false, assert_raises

from sihoo import create_app
from sihoo.exc import SihooDatabaseNotUnique, SihooProgramException
from sihoo.models import db
from sihoo.models.accounts import User
from sihoo.models.chatroom import ChatRoom, ChatRoomMessage


app = create_app(test=True)


def setup():
    with app.app_context():
        db.create_all()
        User.create('azlisme', '123456789')


def test_create_chatroom():
    with app.app_context():
        ChatRoom.create('test chatroom', creator=1, bio='This is test chatroom')


def test_change_chatroom_bio():
    with app.app_context():
        ChatRoom.set_bio(1, 'changed bio')
        pass


def teardown():
    with app.app_context():
        db.metadata.drop_all(db.engine)
