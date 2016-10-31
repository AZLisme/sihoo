# -*- coding: utf-8 -*-
"""


@author: AZLisme
@email:  helloazl@icloud.com
"""

from flask_socketio import SocketIO

socketio = SocketIO()


def configure(app):
    socketio.init_app(app)
