# -*- coding: utf-8 -*-
"""
模型包

@author: AZLisme
@email:  helloazl@icloud.com
"""
import redis

_redis_pool = None


def setup_redis(host: str = '127.0.0.1', port: int = 6379, max_connections: int = 10) -> None:
    """配置全局REDIS配置"""
    global _redis_pool
    _redis_pool = redis.BlockingConnectionPool(host, port, max_connections=max_connections)


def redis_client() -> redis.Redis:
    """获取Redis客户端"""
    global _redis_pool
    return redis.Redis(connection_pool=_redis_pool)
