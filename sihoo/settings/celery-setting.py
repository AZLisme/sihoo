# -*- coding: utf-8 -*-
"""
Sihoo Celery 默认设置

@author: AZLisme
@email:  helloazl@icloud.com
"""


BROKER_URL = 'redis://localhost/1'
CELERY_RESULT_BACKEND = 'redis://localhost/2'

CELERY_IMPORTS = ('sihoo.tasks.email', )
