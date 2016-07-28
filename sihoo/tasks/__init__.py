# -*- coding: utf-8 -*-
"""
Sihoo Celery Worker 模块

@author: AZLisme
@email:  helloazl@icloud.com
"""


from celery import Celery


celery_app = Celery('SihooWorker')


def configure(app):
    celery_app.config_from_object('sihoo.settings.celery-setting')
    celery_app.config_from_envvar('SIHOO_CELERY_SETTINGS', silent=True)
    app.config['CELERY'] = celery_app
