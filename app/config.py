from os import environ, path
from configparser import ConfigParser

basedir = path.abspath(path.dirname(__file__))
database_dir = 'sqlite:///' + path.join(basedir, 'store.db')
config = ConfigParser()
config.read('./settings.ini')

