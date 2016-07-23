# -*- coding: utf-8 -*-
"""
用户账户模型模块

@author: AZLisme
@email:  helloazl@icloud.com
"""

from sihoo.models import db
from sqlalchemy import Column, BigInteger, Sequence, String, Text, DateTime, SmallInteger, Boolean


class User(db.Model):
    __tablename__ = 'users'
    id = Column(BigInteger, Sequence('uid'), primary_key=True)
    name = Column(String)
    password = Column(String)
    gender = Column(SmallInteger)
    reg = Column(DateTime)
    ban = Column(Boolean)
    email = Column(String)
    portrait = Column(String)
    bio = Column(Text)


# class Role(db.Model):
#     pass
#
#
# class EmailVerifyRecord(db.Model):
#     pass
