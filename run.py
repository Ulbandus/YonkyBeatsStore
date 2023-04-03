# -*- coding: utf-8 -*-
from app import app
from app.config import config
from os import environ

app.run(port=environ.get('PORT', int(config['SETTINGS']['port'])),
        host=config['SETTINGS']['host'],
        debug=config['SETTINGS']['debug_mode'])

