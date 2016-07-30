# -*- coding: utf-8 -*-
"""
用户账户相关的视图函数、模块

@author: AZLisme
@email:  helloazl@icloud.com
"""
from flask import Blueprint, flash, jsonify, redirect, render_template, request
from flask_login import login_user, logout_user

from sihoo.exc import SihooDatabaseNotUnique
from sihoo.models.accounts import User
from sihoo.utils.helper import api_result, current_user, set_title
from sihoo.utils.validator import DEFAULT_PASSWORD_CHARSET, DEFAULT_USERNAME_CHARSET, validate_charset

blue_print = Blueprint('sihoo.accounts', __name__, template_folder='templates')


def validate_username(username):
    """
    验证用户名
    :param username: 用户名
    :return: 用户名是否合格
    """
    if len(username) < 3:
        return False
    return validate_charset(username, DEFAULT_USERNAME_CHARSET)


def validate_password(password):
    """
    验证密码
    :param password: 密码
    :return: 密码是否合格
    """
    if len(password) < 6:
        return False
    return validate_charset(password, DEFAULT_PASSWORD_CHARSET)


def extract_username_password():
    """
    提取并验证用户名和密码

    如果验证通过则返回(username, password)，否则返回一个代表着API请求错误的 Response
    :return:
    """
    username = request.form.get('username', type=str)
    password = request.form.get('password', type=str)
    if username is None or password is None:
        return api_result(-1)  # 用户名或密码为空，参数不正确
    if not validate_username(username):
        return api_result(-2)  # 用户名格式不正确
    if not validate_password(password):
        return api_result(-3)  # 密码格式不正确
    return username, password


@blue_print.route('/login', endpoint='login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if current_user().is_authenticated:
            return redirect('/')
        set_title('撕乎 - 登陆')
        return render_template('login.html')
    else:
        result = extract_username_password()
        try:
            username, password = result
        except TypeError:
            return result
        remember = request.form.get('remember', type=bool, default=False)
        if User.verify_password(username, password):
            login_user(User.with_name(username), remember)
            return api_result(1)
        else:
            return api_result(-4)  # 用户名密码不正确


@blue_print.route('/register', endpoint='register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        if current_user().is_authenticated:
            return redirect('/')
        set_title('撕乎 - 注册')
        return render_template('register.html')
    else:
        result = extract_username_password()
        try:
            username, password = result
        except TypeError:
            return result

        try:
            User.create(username, password)
        except SihooDatabaseNotUnique:
            return api_result(-4)  # 用户已经存在
        login_user(User.with_name(username), True)
        return api_result(1)  # 注册成功


@blue_print.route('/logout', endpoint='logout', methods=['GET'])
def logout():
    logout_user()
    flash("您已经成功登出", category='logout')
    return redirect('/')


######################
#
#        API
#
######################


@blue_print.route('/api/unique/<string:username>', endpoint='unique', methods=['GET'])
def user_unique(username):
    return jsonify({'unique': User.query.filter_by(name=username).count() == 0})
