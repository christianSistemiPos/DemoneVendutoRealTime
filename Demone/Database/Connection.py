from pony.orm import *
import json
import sys

from config import configuration

db = Database()
database_out = configuration['out']['database']

connection = db.bind(provider='mysql',
                     host=database_out['db_address'],
                     user=database_out['db_username'],
                     password=database_out['db_password'],
                     db=database_out['db_name'],
                     port=database_out['db_port']
                     )