# -*- coding: utf-8 -*-
"""
模型包

@author: AZLisme
@email:  helloazl@icloud.com
"""

from flask_sqlalchemy import SQLAlchemy
from redis import Redis, BlockingConnectionPool

db = SQLAlchemy()
_redis_pool = None


def configure_redis(app):
    global _redis_pool
    REDIS_HOST = app.config.get("REDIS_HOST")
    REDIS_PORT = app.config.get("REDIS_PORT")
    _redis_pool = BlockingConnectionPool(host=REDIS_HOST, port=REDIS_PORT)


def redis_client() -> Redis:
    global  _redis_pool
    return Redis(connection_pool=_redis_pool)

import sihoo.models.accounts
import sihoo.models.si
import sihoo.models.chatroom
