# -*- coding: utf-8 -*-
"""
用户账户相关的视图函数、模块

@author: AZLisme
@email:  helloazl@icloud.com
"""


from flask import Blueprint, request, render_template, jsonify


blue_print = Blueprint('sihoo.accounts', __name__, template_folder='templates')


@blue_print.route('/login', endpoint='login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        return jsonify(msg='Under construction!')
