# -*- coding: utf-8 -*-
"""
用户账户模型模块

@author: AZLisme
@email:  helloazl@icloud.com
"""

from sqlalchemy import BigInteger, Boolean, Column, DateTime, Index, Sequence, SmallInteger, String, Text, func
from sqlalchemy.exc import IntegrityError

from sihoo.exc import SihooDatabaseNotUnique
from sihoo.models import db
from sihoo.utils.auth import hash_password, verify_password
from sihoo.utils.time import now


class User(db.Model):
    __tablename__ = 'users'
    id = Column(BigInteger, Sequence('users.id'), primary_key=True)
    name = Column(String)
    password = Column(String)
    salt = Column(String)
    gender = Column(SmallInteger, nullable=True)
    reg = Column(DateTime)
    ban = Column(Boolean, default=False)
    email = Column(String, nullable=True)
    portrait = Column(String, nullable=True)
    bio = Column(Text, default="")
    __table_args__ = (
        Index('username_unique', func.lower(name), unique=True),
    )

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return not self.ban

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    @classmethod
    def create(cls, name, password):
        """创建一个新的用户"""
        session = db.session()
        hashed, salt = hash_password(password)
        session.add(cls(name=name, password=hashed, salt=salt, reg=now()))
        try:
            session.commit()
        except IntegrityError:
            raise SihooDatabaseNotUnique

    @classmethod
    def verify_password(cls, username, password):
        """验证用户的用户名密码"""
        user = db.session.query(User.password, User.salt).filter(User.name == username).first()
        if user is None:
            return False
        return verify_password(password, user.password, user.salt)

    @classmethod
    def with_name(cls, name):
        """获取该名字的用户对象"""
        try:
            name = str(name)
        except TypeError:
            return None
        return User.query.filter_by(name=name).first()

    @classmethod
    def with_id(cls, uid):
        """获取该ID的用户对象"""
        if not isinstance(uid, int):
            try:
                uid = int(uid)
            except TypeError:
                return None
        return User.query.filter_by(id=uid).first()

    @classmethod
    def user_count(cls):
        """获取用户总数"""
        return User.query.count()
