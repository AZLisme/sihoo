# -*- coding: utf-8 -*-
"""
Flask App 相关默认配置文件

@author: AZLisme
@email:  helloazl@icloud.com
"""

# Flask Settings
SECRET_KEY = 'secret'

# Database Setting
SQLALCHEMY_DATABASE_URI = "postgresql+pygresql://postgres:azlisme@localhost/sihoo_db"

# Redis Settings
REDIS_HOST = "localhost"
REDIS_PORT = "6379"
REDIS_USER = ""
REDIS_PASSWORD = ""

# SQLAlchemy
SQLALCHEMY_TRACK_MODIFICATIONS = False
