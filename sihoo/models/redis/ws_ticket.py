# -*- coding: utf-8 -*-
"""
Web socket ticket

@author: AZLisme
@email:  helloazl@icloud.com
"""

import uuid

from . import redis_client


class WebsocketTicket(object):
    """
    Websocket Ticket 是一种数据抽象，用于Tornado验证Flask的用户凭证。

    在验证请求创建时写入一个Ticket，并将Ticket ID返回给Web请求。
    Tornado验证此凭证时，通过ID获取Ticket信息（用户、频道）并且通过验证
    """
    def __init__(self, room: str, uid: str, expire: int = 60, _uuid: str = None):
        self.room = room
        self.uid = uid
        self.expire = expire
        self.uuid = _uuid

    def serial(self):
        return '{}|{}'.format(self.uid, self.room)

    @classmethod
    def loads(cls, uuid: str, value: str):
        s = value.split('|')
        return cls(uuid=uuid, uid=s[0], room=s[1])


class WebsocketTicketManager(object):

    @staticmethod
    def save(ticket: WebsocketTicket) -> str:
        """将Ticket保存至Redis

        :param ticket: 要保存的Ticket对象
        :return: Ticket 的 UUID
        """
        redis = redis_client()
        _uuid = ticket.uuid
        if _uuid is None:
            _uuid = str(uuid.uuid1())
        redis.set(ticket.uuid, ticket.serial(), ex=ticket.expire)
        ticket.uuid = _uuid
        return _uuid

    @staticmethod
    def lookup(_uuid: str, delete=True) -> WebsocketTicket:
        """从Redis中查找Ticket

        :param _uuid: 要查找的UUID
        :param delete: 查找成功后是否删除该Ticket
        :return: 如果找到，则返回该Ticket，如果没找到，则返回None
        """
        value = redis_client().get(_uuid)
        if value is None:
            return None
        if delete:
            redis_client().delete(_uuid)
        return WebsocketTicket.loads(_uuid, value)

