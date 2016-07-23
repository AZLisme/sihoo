# -*- coding: utf-8 -*-
"""
Flask App 相关默认配置文件

@author: AZLisme
@email:  helloazl@icloud.com
"""

HOST = "0.0.0.0"
PORT = 8080

# Flask Settings
STATIC_FOLDER = '../front'

# PostgreSQL Settings
POSTGRESQL_HOST = "localhost"
POSTGRESQL_PORT = 6379
POSTGRESQL_USER = "username"
POSTGRESQL_PASSWORD = "password"

# Redis Settings
REDIS_HOST = "localhost"
REDIS_PORT = ""
REDIS_USER = "username"
REDIS_PASSWORD = "password"

# SQLAlchemy
SQLALCHEMY_TRACK_MODIFICATIONS = False
