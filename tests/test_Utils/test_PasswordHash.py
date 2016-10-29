# -*- coding: utf-8 -*-
"""


@author: AZLisme
@email:  helloazl@icloud.com
"""

from sihoo.utils.auth import hash_password, verify_password


def test_password_hash():
    hashed, salt = hash_password('correct')
    assert verify_password('correct', hashed, salt)
    assert not verify_password('incorrect', hashed, salt)
    assert not verify_password('correct', hashed, 'not salt')
    assert not verify_password('correct', 'not hashed', salt)
