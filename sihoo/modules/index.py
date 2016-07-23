# -*- coding: utf-8 -*-
"""


@author: AZLisme
@email:  helloazl@icloud.com
"""


from flask import Blueprint, request, render_template


blue_print = Blueprint('sihoo.index', __name__, template_folder='templates')


@blue_print.route('/', endpoint='home')
def home():
    return render_template('index.html')
