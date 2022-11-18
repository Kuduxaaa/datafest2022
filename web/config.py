# -*- coding: utf-8 -*-

class Config(object):
    DEBUG = False
    TESTING = False
    SITE_NAME = 'Data Visualisation'
    SECRET_KEY = 'c219d4e3-3ea8-4dbb-8641-8bbfc644aa18'
    API_PREFIX = '/api/v1'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True