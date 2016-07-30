# -*- coding: utf-8 -*-
"""


@author: AZLisme
@email:  helloazl@icloud.com
"""

from string import ascii_letters, digits, punctuation

DEFAULT_USERNAME_CHARSET = ascii_letters + digits + '_'
DEFAULT_PASSWORD_CHARSET = ascii_letters + digits + punctuation


def validate_charset(s, charset=DEFAULT_USERNAME_CHARSET):
    """
    确认给定字符串字符集全在charset中
    :param s: 待确认字符串
    :param charset: 字符集
    :return:
    """
    chars = list(set(s))
    return False not in [c in charset for c in chars]
