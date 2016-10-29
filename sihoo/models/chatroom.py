# -*- coding: utf-8 -*-
"""
聊天室模型

@author: AZLisme
@email:  helloazl@icloud.com
"""

from sqlalchemy import String, Integer, Column, Text, DateTime, ForeignKey, BigInteger, Index, Sequence
from sqlalchemy.exc import IntegrityError

from sihoo.exc import SihooDatabaseNotUnique, SihooProgramException
from sihoo.models import db
from sihoo.models.accounts import User
from sihoo.utils.time import now


class ChatRoom(db.Model):
    __tablename__ = 'chatroom'
    cid = Column(Integer, Sequence('chatroom.cid'), primary_key=True)
    name = Column(String)
    bio = Column(Text)
    reg_date = Column(DateTime)
    creator = Column(ForeignKey(User.id, ondelete="SET NULL"))

    @classmethod
    def create(cls, name, creator, bio=""):
        session = db.Session()
        session.add(cls(name=name, bio=bio, creator=creator, reg_date=now()))
        try:
            session.commit()
        except IntegrityError:
            raise SihooDatabaseNotUnique

    @classmethod
    def with_id(cls, id):
        if not isinstance(id, int):
            try:
                id = int(id)
            except TypeError:
                return None
        return ChatRoom.query.filter_by(cid=id).first()

    @classmethod
    def set_bio(cls, cid, bio):
        session = db.Session()
        room = User.with_id(cid)
        if not room:
            return
        room.bio = bio
        session.commit()


class ChatRoomMessage(db.Model):
    __tablename__ = 'chatroom_msg'
    mid = Column(BigInteger, Sequence('chatroom_msg.mid'), primary_key=True)
    cid = Column(ForeignKey(ChatRoom.cid, ondelete="CASCADE"))
    uid = Column(ForeignKey(User.id, ondelete="CASCADE"))
    content = Column(Text)
    time = Column(DateTime)
    __table_args__ = (
        Index('chat_seq', cid, time),
    )

    @classmethod
    def new(cls, cid, uid, content):
        session = db.Session()
        msg = cls(cid=cid, uid=uid, content=content, time=now())
        session.add(msg)
        session.commit()

    @classmethod
    def history_of(cls, chatroom, frm=None, size=100):
        cid = None
        if isinstance(chatroom, ChatRoom):
            cid = chatroom.cid
        else:
            try:
                cid = int(chatroom)
            except TypeError:
                raise SihooProgramException("Can't convert chatroom into Chatroom.cid")
        if frm is not None:
            if isinstance(frm, cls):
                fid = frm.mid
            else:
                try:
                    fid = int(frm)
                except TypeError:
                    raise SihooProgramException("Can't convert frm into ChatRoomMessage.mid")
            cls.query(cid=cid)
