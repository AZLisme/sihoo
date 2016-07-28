# -*- coding: utf-8 -*-
"""


@author: AZLisme
@email:  helloazl@icloud.com
"""

from sihoo import make_flask_app
from sihoo.models import db


app = make_flask_app(test=True)


def test_create_table():
    with app.app_context():
        db.create_all()
