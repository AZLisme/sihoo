# -*- coding: utf-8 -*-
"""


@author: AZLisme
@email:  helloazl@icloud.com
"""

from tornado.websocket import WebSocketHandler


class SihooWebSocketHandler(WebSocketHandler):
    def open(self, *args, **kwargs):
        pass

    def on_message(self, message):
        pass

    def on_close(self):
        pass

    def select_subprotocol(self, subprotocols):
        pass
