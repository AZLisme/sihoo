# -*- coding: utf-8 -*-
"""


@author: AZLisme
@email:  helloazl@icloud.com
"""


class SihooBaseException(Exception):
    pass


class SihooProgramException(SihooBaseException):
    pass


class SihooDatabaseException(SihooBaseException):
    pass


class SihooDatabaseNotUnique(SihooDatabaseException):
    pass


class SihooDatabaseNoResult(SihooDatabaseException):
    pass
