from pony.orm import *
from datetime import time,datetime
from Database import db

class TableAnomalia(db.Entity):
    _table_ = "anomalie_vrt"

    id_cassa = Required(str, 100)
    id_negozio = Required(str, 100)
    id_cliente = Required(str, 100)
    ora_anomalia = Optional(time)
    operatore = Optional(str,255)
    descrizione_anomalia = Required(str)
    tipo_anomalia = Required(str,100)
    id_anomalia = Required(str)
    PrimaryKey(id_anomalia)