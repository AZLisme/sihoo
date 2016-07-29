# -*- coding: utf-8 -*-
"""


@author: AZLisme
@email:  helloazl@icloud.com
"""

from flask import g


def set_title(title):
    """设定页面的标题"""
    g.title = title