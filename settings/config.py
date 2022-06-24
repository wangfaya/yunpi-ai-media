# -*- coding: UTF-8 -*-

import os
import time

PLATFORM_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

###
# Log config
###
LOG_LEVEL = "WARNING"
LOG_DIR = os.path.join(PLATFORM_DIR, "logs")
LOG_SYS_PATH = os.path.join(LOG_DIR, "sys_" + time.strftime("%Y-%m-%d", time.localtime()) + ".log")

###
# Flask Server config
###
DEBUG = False
HOST = '127.0.0.1'
PORT = 9999
STATIC_FOLDER = os.path.join(PLATFORM_DIR, 'server/static')
TEMPLATE_FOLDER = os.path.join(PLATFORM_DIR, 'server/templates')
STATIC_URL_PATH = '/backend'

