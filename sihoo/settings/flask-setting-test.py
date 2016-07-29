# -*- coding: utf-8 -*-
"""
Flask App 相关默认配置文件(测试用)

@author: AZLisme
@email:  helloazl@icloud.com
"""

HOST = "0.0.0.0"
PORT = 8080

# Flask Settings
STATIC_FOLDER = '../front'
STATIC_URL_PATH = 'static'


SQLALCHEMY_DATABASE_URI = "postgresql://sihoo_test:sihoo_test@localhost/sihoo_test"


# Redis Settings
REDIS_HOST = "localhost"
REDIS_PORT = ""
REDIS_USER = "username"
REDIS_PASSWORD = "password"

# SQLAlchemy
SQLALCHEMY_TRACK_MODIFICATIONS = False
