import os
import json

with open('/path/to/config/') as config_file:
	config = json.load(config_file)

class Config:
    SECRET_KEY = config.get('SECRET_KEY')
