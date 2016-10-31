# -*- coding: utf-8 -*-
"""


@author: AZLisme
@email:  helloazl@icloud.com
"""

from flask import Blueprint, render_template, request

from sihoo.models.chatroom import ls_chatroom

blue_print = Blueprint('sihoo.index', __name__, template_folder='templates')


@blue_print.route('/', endpoint='home', methods=['GET'])
def home():
    return render_template('index.html')


@blue_print.route('/plaza', endpoint='plaza', methods=['GET'])
def plaza():
    return render_template('roomlist.html', roomlist=ls_chatroom())


@blue_print.route('/follow', endpoint='follow', methods=['GET'])
def follows():
    return render_template('construction.html')

