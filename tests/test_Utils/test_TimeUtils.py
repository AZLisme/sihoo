# -*- coding: utf-8 -*-
"""
This module tests if time utlis works properly

@author: AZLisme
@email:  helloazl@icloud.com
"""

import time
from datetime import datetime

import pytz

from sihoo.utils.time import timestamp, set_default_timezone, datetime_from_timestamp


def test_timestamp():
    assert abs(timestamp() - time.time()) < 0.1
    assert abs(timestamp(datetime.utcnow()) - time.time()) < 0.1
    assert timestamp(datetime(1970, 1, 1, 0, 0, 1, 0)) - 1.0 < 0.1


def test_convert():
    # 时间戳 1469264524, 北京时间 2016/7/23 17:2:4
    dt1 = datetime_from_timestamp(1469264524)
    dt1 = dt1.astimezone(pytz.timezone('Asia/Shanghai'))
    assert dt1.year == 2016
    assert dt1.month == 7
    assert dt1.day == 23
    assert dt1.hour == 17
    assert dt1.minute == 2
    assert dt1.second == 4


def test_set_default_timezone():
    set_default_timezone('UTC')
    dt1 = datetime_from_timestamp(1)
    assert dt1.tzname() == 'UTC'
    assert dt1.hour == 0
    set_default_timezone('Asia/Shanghai')
    dt1 = datetime_from_timestamp(1)
    assert dt1.tzname() == 'CST'
    assert dt1.hour == 8
    # 将默认时区改回标准UTC时间
    set_default_timezone('UTC')
