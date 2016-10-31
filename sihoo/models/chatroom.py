# -*- coding: utf-8 -*-
"""
聊天室模型, 基于内存数据库Redis

@author: AZLisme
@email:  helloazl@icloud.com
"""

from sihoo.models import redis_client
import time

CHATROOM_SET = '_CHATROOM_SET'
CHATROOM_MEMBER_PRE = "_CMB_"
CHATROOM_MESSAG_PRE = "_CMS_"


def add_chatroom(name):
    db = redis_client()
    return db.sadd(CHATROOM_SET, name)


def del_chatroom(name):
    db = redis_client()
    return db.srem(CHATROOM_SET, name)


def ls_chatroom():
    db = redis_client()
    return map(lambda x: x.decode('utf-8'), db.smembers(CHATROOM_SET))


def ck_chatroom(name):
    db = redis_client()
    return db.sismember(CHATROOM_SET, name)


def add_user(uid, chatroom):
    db = redis_client()
    return db.hincrby(CHATROOM_MEMBER_PRE + chatroom, uid)


def ls_user(chatroom):
    db = redis_client()
    return db.hkeys(CHATROOM_MEMBER_PRE + chatroom)


def rm_user(uid, chatroom):
    db = redis_client()
    lock = db.lock(CHATROOM_MEMBER_PRE + chatroom)
    db.hincrby(CHATROOM_MEMBER_PRE + chatroom, uid, amount=-1)
    if db.hget(CHATROOM_MEMBER_PRE + chatroom, uid) == "0":
        db.hdel(CHATROOM_MEMBER_PRE + chatroom, uid)
    lock.release()


def add_message(chatroom, uid, msg):
    db = redis_client()
    time_id = int(time.time() / 1800)
    key = CHATROOM_MESSAG_PRE + chatroom + str(time_id)
    existed = False
    if not db.exists(key):
        existed = True
    db.lpush(key, "{}#{}#{}".format(uid, str(int(time.time())), msg))
    if not existed:
        db.expire(key, 1860) # 留出60秒安全时间


def ls_message(chatroom):
    db = redis_client()
    time_id = int(time.time() / 1800)
    key_now = CHATROOM_MESSAG_PRE + chatroom + str(time_id)
    key_pre = CHATROOM_MESSAG_PRE + chatroom + str(time_id - 1)
    ls_now = db.lrange(key_now, 0, -1)
    ls_pre = db.lrange(key_pre, 0, -1)
    if ls_pre:
        ls_now += ls_pre
    return map(lambda x: x.split('#', maxsplit=2), ls_now)

# from sqlalchemy import String, Integer, Column, Text, DateTime, ForeignKey, BigInteger, Index, Sequence
# from sqlalchemy.exc import IntegrityError
#
# from sihoo.exc import SihooDatabaseNotUnique, SihooProgramException
# from sihoo.models import db
# from sihoo.models.accounts import User
# from sihoo.utils.time import now
#
#
# class ChatRoom(db.Model):
#     __tablename__ = 'chatroom'
#     cid = Column(Integer, Sequence('chatroom.cid'), primary_key=True)
#     name = Column(String)
#     bio = Column(Text)
#     reg_date = Column(DateTime)
#     creator = Column(ForeignKey(User.id, ondelete="SET NULL"))
#
#     @classmethod
#     def create(cls, name, creator, bio=""):
#         session = db.session()
#         session.add(cls(name=name, bio=bio, creator=creator, reg_date=now()))
#         try:
#             session.commit()
#         except IntegrityError:
#             raise SihooDatabaseNotUnique
#
#     @classmethod
#     def with_id(cls, id):
#         if not isinstance(id, int):
#             try:
#                 id = int(id)
#             except TypeError:
#                 return None
#         return ChatRoom.query.filter_by(cid=id).first()
#
#     @classmethod
#     def set_bio(cls, cid, bio):
#         session = db.session()
#         room = User.with_id(cid)
#         if not room:
#             return
#         room.bio = bio
#         session.commit()
#
#
# class ChatRoomMessage(db.Model):
#     __tablename__ = 'chatroom_msg'
#     mid = Column(BigInteger, Sequence('chatroom_msg.mid'), primary_key=True)
#     cid = Column(ForeignKey(ChatRoom.cid, ondelete="CASCADE"))
#     uid = Column(ForeignKey(User.id, ondelete="CASCADE"))
#     content = Column(Text)
#     time = Column(DateTime)
#     __table_args__ = (
#         Index('chat_seq', cid, time),
#     )
#
#     @classmethod
#     def new(cls, cid, uid, content):
#         session = db.session()
#         msg = cls(cid=cid, uid=uid, content=content, time=now())
#         session.add(msg)
#         session.commit()
#
#     @classmethod
#     def history_of(cls, chatroom, frm=None, size=100):
#         cid = None
#         if isinstance(chatroom, ChatRoom):
#             cid = chatroom.cid
#         else:
#             try:
#                 cid = int(chatroom)
#             except TypeError:
#                 raise SihooProgramException("Can't convert chatroom into Chatroom.cid")
#         if frm is not None:
#             if isinstance(frm, cls):
#                 fid = frm.mid
#             else:
#                 try:
#                     fid = int(frm)
#                 except TypeError:
#                     raise SihooProgramException("Can't convert frm into ChatRoomMessage.mid")
#             cls.query(cid=cid).sort_by(cls.time)
