# -*- coding: utf-8 -*-
"""
时间处理模块，统一处理时间相关函数

@author: AZLisme
@email:  helloazl@icloud.com
"""

from datetime import datetime, timedelta
import pytz
import time


_DEFAULT_TIMEZONE = pytz.utc


def now(tz=None):
    """获取现在的日期对象（带时区）"""
    if tz is None:
        return datetime.now(tz=_DEFAULT_TIMEZONE)
    else:
        return datetime.now(tz=tz)


def get_timezone(tz_name: str):
    """获取时区对象，封装pytz

    :param tz_name: 时区名字，常用的有'UTC', 'Asia/Shanghai'
    :return:
    """
    return pytz.timezone(tz_name)


def get_default_timezone():
    """获取默认时间戳

    :return:
    """
    return _DEFAULT_TIMEZONE


def set_default_timezone(tz_name: str) -> None:
    """设置默认的时区

    :param Union(str, unicode) tz_name: 时区名字, 例如 'UTC', 'Asia/Shanghai'
    :return: None
    """
    global _DEFAULT_TIMEZONE
    _DEFAULT_TIMEZONE = pytz.timezone(tz_name)


def timestamp(dt: datetime = None) -> float:
    """获取时间戳, 如果参数为None则返回当前时间戳

    :param dt: 要转化为时间戳的时间，如果为None则返回当前时间戳。
    :return float: 时间戳
    """
    if dt is None:
        return time.time()
    else:
        if dt.tzinfo is None:
            dt = _DEFAULT_TIMEZONE.localize(dt)
        utc_dt = dt.astimezone(pytz.utc)
        delta = utc_dt - datetime(1970, 1, 1, 0, 0 ,0, 0, pytz.utc)
        return delta.total_seconds()


def datetime_from_timestamp(ts: float) -> datetime:
    """ 从时间戳获取日期对象

    :param ts: 时间戳
    :return: 日期对象
    """
    dt = datetime(1970, 1, 1, 0, 0 ,0, 0, pytz.utc) + timedelta(seconds=ts)
    return dt.astimezone(_DEFAULT_TIMEZONE)
