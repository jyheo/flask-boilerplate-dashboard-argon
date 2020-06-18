# -*- encoding: utf-8 -*-
"""
License: Commercial
Copyright (c) 2019 - present AppSeed.us
"""

from flask_migrate import Migrate
from os import environ
from sys import exit

from config import config_dict
from app import create_app, db

# config_mode = config_dict['Production']
config_mode = config_dict['Debug']

app = create_app(config_mode) 
Migrate(app, db)

if __name__ == "__main__":
    app.run()
