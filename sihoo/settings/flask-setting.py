# -*- coding: utf-8 -*-
"""
Flask App 相关默认配置文件

@author: AZLisme
@email:  helloazl@icloud.com
"""

# Flask Settings
SECRET_KEY = 'secret'

SQLALCHEMY_DATABASE_URI = "postgresql://sihoo:sihoo@localhost/sihoo"

# Redis Settings
REDIS_HOST = "localhost"
REDIS_PORT = ""
REDIS_USER = "username"
REDIS_PASSWORD = "password"

# SQLAlchemy
SQLALCHEMY_TRACK_MODIFICATIONS = False
