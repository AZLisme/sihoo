# -*- coding: utf-8 -*-
"""


@author: AZLisme
@email:  helloazl@icloud.com
"""

import uuid

import hashlib


def hash_password(password, salt=None):
    """为密码加盐并返回"""
    if salt is None:
        salt = uuid.uuid4().hex
    hashed_password = hashlib.sha512((password + salt).encode('ascii')).hexdigest()
    return (hashed_password, salt)


def verify_password(password, hashed_password, salt):
    """验证密码是否正确"""
    re_hashed, salt = hash_password(password, salt)
    return re_hashed == hashed_password
