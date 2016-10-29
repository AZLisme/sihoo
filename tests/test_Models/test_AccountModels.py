# -*- coding: utf-8 -*-
"""


@author: AZLisme
@email:  helloazl@icloud.com
"""
from nose.tools import assert_false, assert_raises

from sihoo import create_app
from sihoo.exc import SihooDatabaseNotUnique
from sihoo.models import db
from sihoo.models.accounts import User

app = create_app(test=True)


def setup():
    with app.app_context():
        db.create_all()


def test_insensitive_username():
    with app.app_context():
        User.create(name='Azlisme', password='azlisme')
        User.create(name='AZlisme123', password='azlisme')
        assert_raises(SihooDatabaseNotUnique, User.create, name='AZLISME', password='azlisme')


def test_verify_user_password():
    with app.app_context():
        username, password = 'testUser', 'password'
        User.create(name=username, password=password)
        assert User.verify_password(username, password)
        assert_false(User.verify_password(username, 'wrongPassword'))
        assert_false(User.verify_password('not_exist', password))


def test_query_user():
    with app.app_context():
        assert User.with_id(1) is not None
        assert User.with_id('1') is not None
        assert User.with_name('Azlisme') is not None

        assert User.with_id(100) is None
        assert User.with_id('100') is None
        assert User.with_name('azlisme') is None
        assert User.with_name('notExistUser') is None
        assert User.with_name(123) is None
        assert User.with_name(None) is None
        assert User.with_name(app) is None


def test_query_user_count():
    with app.app_context():
        User.query.delete()
        assert User.user_count() == 0
        User.create('azlisme', 'azlisme')
        assert User.user_count() == 1
        [User.create('azlisme' + str(i), 'azlisme') for i in range(0, 10)]
        assert User.user_count() == 11


def teardown():
    with app.app_context():
        db.metadata.drop_all(db.engine)
