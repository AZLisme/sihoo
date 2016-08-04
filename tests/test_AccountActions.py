# -*- coding: utf-8 -*-
"""


@author: AZLisme
@email:  helloazl@icloud.com
"""
from flask import json

from sihoo import make_flask_app
from sihoo.models import db
from sihoo.models.accounts import User

app = make_flask_app(test=True)

client = app.test_client()


def setup():
    with app.app_context():
        db.create_all()


def test_page_available():
    assert '我同意《撕乎使用协议》' in str(client.get('/register').data, encoding='utf-8')
    assert '记住我' in str(client.get('/login').data, encoding='utf-8')


def request_and_get_result(d, url='/register'):
    rv = json.loads(client.post(url, data=d).data)
    return rv.get('result')


def c(username, password):
    return dict(username=username, password=password)


def test_register_api():
    assert request_and_get_result(c('azlisme', 'azlisme')) == 1
    assert request_and_get_result(c('azlisme', 'azlisme')) == -4  # 用户已经存在
    assert request_and_get_result(c('Azlisme', 'azlisme')) == -4  # 用户已经存在
    assert request_and_get_result(c('azlisme', 'azlisme123')) == -4  # 用户已经存在
    assert request_and_get_result(c('a', 'azlisme123')) == -2  # 用户名格式不正确
    assert request_and_get_result(c('a#@', 'azlisme123')) == -2  # 用户名格式不正确
    assert request_and_get_result(c('azlisme', 'a\n\t')) == -3  # 密码格式不正确
    assert request_and_get_result(c('a\nt', 'a\n\t')) == -2  # 用户名密码格式都不正确

    # 注册信息缺失
    assert request_and_get_result(dict()) == -1
    assert request_and_get_result(dict(username='a')) == -1
    assert request_and_get_result(dict(password='a')) == -1
    assert request_and_get_result(dict(username='azlisme')) == -1
    assert request_and_get_result(dict(password='azlisme')) == -1

    # 确认只注册成功了一个用户
    with app.app_context():
        assert User.user_count() == 1

    # 尝试再注册一个用户
    assert request_and_get_result(c('azlisme1', 'azlisme1')) == 1
    with app.app_context():
        assert User.user_count() == 2


def test_login_api():
    # 登陆信息缺失
    assert request_and_get_result(dict(), url='/login') == -1
    assert request_and_get_result(dict(username='a'), url='/login') == -1
    assert request_and_get_result(dict(password='a'), url='/login') == -1
    assert request_and_get_result(dict(username='azlisme'), url='/login') == -1
    assert request_and_get_result(dict(password='azlisme'), url='/login') == -1

    assert request_and_get_result(c('a', 'azlisme123'), url='/login') == -2  # 用户名格式不正确
    assert request_and_get_result(c('a#@', 'azlisme123'), url='/login') == -2  # 用户名格式不正确
    assert request_and_get_result(c('azlisme', 'a\n\t'), url='/login') == -3  # 密码格式不正确
    assert request_and_get_result(c('a\nt', 'a\n\t'), url='/login') == -2  # 用户名密码格式都不正确

    # 用户密码不正确
    assert request_and_get_result(c('azlisme', 'azlisme123'), url='/login') == -4

    # 正确登陆
    assert request_and_get_result(c('azlisme', 'azlisme'), url='/login') == 1
    assert 'azlisme' in str(client.get('/').data, encoding='utf-8')

    # 变名登陆, 用户名大小写敏感
    assert request_and_get_result(c('Azlisme', 'azlisme'), url='/login') == -4


def test_auto_redirect_if_logged_in():
    # 经过之前的测试，目前用户已经登陆
    assert '我同意撕乎使用协议' not in str(client.get('/register', follow_redirects=True).data, encoding='utf-8')
    assert '记住我' not in str(client.get('/login', follow_redirects=True).data, encoding='utf-8')
    assert 'azlisme' in str(client.get('/register', follow_redirects=True).data, encoding='utf-8')
    assert 'azlisme' in str(client.get('/login', follow_redirects=True).data, encoding='utf-8')
    assert '广场' in str(client.get('/register', follow_redirects=True).data, encoding='utf-8')
    assert '广场' in str(client.get('/login', follow_redirects=True).data, encoding='utf-8')


def test_logout():
    # 经过之前的测试，目前用户已经登陆
    rv = client.get('/logout')
    assert rv.status_code == 302
    assert '注册' in str(client.get('/').data, encoding='utf-8')


def teardown():
    with app.app_context():
        db.drop_all()
