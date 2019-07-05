""" config.py """
import json


def open_config(config_file=None):
    try:
        filename = config_file or '.env'
        config_data = open(filename, 'r')
        print('Target configuration file: ' + filename)
        return json.loads(config_data.read())
    except Exception as e:
        print('Configuration file error: ' + str(e))
        return {}


class Environment():
    def __init__(self):
        configuration = open_config() or {}
        self.app_host = configuration.get('host', '0.0.0.0')
        self.app_port = configuration.get('port', 5000)
        self.environment = configuration.get('env', 'dev')


config = Environment()
