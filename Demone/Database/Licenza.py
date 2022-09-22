"""
Modello per la gestione della licenza software
"""
import json
import sys
from typing import List, Tuple
from datetime import date
from config import configuration
import logging

from pony.orm import *

licenze_db = Database()

class TableLicenza(licenze_db.Entity):
    _table_ = "SP_LICENZE"

    id_app = Required(str, 50)
    id_cliente = Required(str, 50)
    codice_negozio = Required(str, 10)
    id_postazione = Required(str, 50)
    data_fine_licenza = Required(date)
    id_licenza = Optional(str,255)
    buffer_info = Optional(str,1000)
    PrimaryKey(id_app, id_cliente, codice_negozio, id_postazione)
    
    def id_valida(self):
        self.negozi = list(filter(lambda id_negozio: len(id_negozio) > 0, self.buffer_info.split(";")))
        return False if len(self.negozi) == 0 else True 
    
licenza = configuration['licenze']['database']
connection = licenze_db.bind(provider='mysql',
                    host=licenza['db_address'],
                    user=licenza['db_username'],
                    password=licenza['db_password'],
                    db=licenza['db_name'],
                    port=licenza['db_port']
                     )
licenze_db.generate_mapping(create_tables=True)
