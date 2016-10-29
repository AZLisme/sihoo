# -*- coding: utf-8 -*-
"""


@author: AZLisme
@email:  helloazl@icloud.com
"""

from sihoo.utils.validator import DEFAULT_USERNAME_CHARSET, validate_charset


def test_charset_validator():
    assert validate_charset('12345678', DEFAULT_USERNAME_CHARSET)
    assert validate_charset('abcABC123', DEFAULT_USERNAME_CHARSET)
    assert validate_charset('ABCDEFG', DEFAULT_USERNAME_CHARSET)
    assert validate_charset('aaaaaaa', DEFAULT_USERNAME_CHARSET)
    assert not validate_charset('df###dfafdsf', DEFAULT_USERNAME_CHARSET)
    assert not validate_charset('abc<hello>', DEFAULT_USERNAME_CHARSET)
    assert not validate_charset('yesthis<zx>', DEFAULT_USERNAME_CHARSET)
