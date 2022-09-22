from pony.orm import *
from datetime import datetime
from Database import db

class TableNegozio(db.Entity):
    _table_ = "negozio"

    id_negozio = Required(str, 100)
    id_cliente = Required(str, 100)
    nome_negozio = Required(str, 100)
    ultimo_aggiornamento = Required(datetime)
    chiuso = Required(bool)
    livello_max_fidelity = Required(int)
    versione_demone = Optional(str,100)
    PrimaryKey(id_negozio,id_cliente)