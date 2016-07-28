# -*- coding: utf-8 -*-
"""
撕逼模型模块

@author: AZLisme
@email:  helloazl@icloud.com
"""

from sqlalchemy import Column, BigInteger, Sequence, String, ForeignKey, DateTime, Text, Boolean

from sihoo.models import db
from sihoo.models.accounts import User


class Si(db.Model):
    __tablename__ = 'si'
    id = Column(BigInteger, Sequence('si.id'), primary_key=True)
    slug = Column(String(64), unique=True)
    creator = Column(ForeignKey(User.id))
    against = Column(ForeignKey(User.id))
    created = Column(DateTime)
    title = Column(String)
    public = Column(Boolean)
    finish = Column(Boolean)
    bio = Column(Text)


class UserToSi(db.Model):
    __tablename__ = 'user_si'
    uid = Column(ForeignKey(User.id, ondelete='CASCADE'), primary_key=True)
    sid = Column(ForeignKey(Si.id, ondelete='CASCADE'), primary_key=True)
    dt = Column(DateTime)
    side = Column(Boolean)


class Argue(db.Model):
    __tablename__ = 'argue'
    id = Column(BigInteger, Sequence('argue.id'), primary_key=True)
    uid = Column(ForeignKey(User.id))
    sid = Column(ForeignKey(Si.id))
    posted = Column(DateTime)
    against = Column(ForeignKey('argue.id', ondelete='RESTRICT'))
    side = Column(Boolean)
    content = Column(Text)


class Vote(db.Model):
    __tablename__ = 'vote'
    uid = Column(ForeignKey(User.id, ondelete='CASCADE'), primary_key=True)
    sid = Column(ForeignKey(Si.id, ondelete='CASCADE'), primary_key=True)
    ts = Column(DateTime)
    support = Column(Boolean)


class VoteTotal(db.Model):
    __tablename__ = 'vote_total'
    sid = Column(ForeignKey(Si.id, ondelete='CASCADE'), primary_key=True)
    a = Column(BigInteger)
    b = Column(BigInteger)
