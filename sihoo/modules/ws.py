# -*- coding: utf-8 -*-
"""


@author: AZLisme
@email:  helloazl@icloud.com
"""

from tornado.websocket import WebSocketHandler


class SihooWebSocketHandler(WebSocketHandler):
    clients = dict()

    def __init__(self):
        super(SihooWebSocketHandler, self).__init__()
        self.room = 'default'

    def open(self, *args, **kwargs):
        room = self.get_query_argument('room')
        self.room = room
        clients = SihooWebSocketHandler.clients
        if room not in clients:
            clients[room] = list()
        clients[room].append(self)

    def on_message(self, message):
        pass

    def on_close(self):
        room = self.room
        clients = SihooWebSocketHandler.clients
        if room in clients:
            clients[room].remove(self)

    @classmethod
    def send_message(cls, room, message):
        for client in cls.clients[room]:
            client.write_message(message)
