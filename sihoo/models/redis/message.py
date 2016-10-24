# -*- coding: utf-8 -*-
"""


@author: AZLisme
@email:  helloazl@icloud.com
"""


class BaseMessage(object):

    def __init__(self, ts, tp):
        self.ts = ts
        self.tp = tp


class SibiMessage(BaseMessage):
    pass