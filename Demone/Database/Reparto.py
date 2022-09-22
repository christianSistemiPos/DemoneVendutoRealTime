from pony.orm import *
from Database import db


class TableReparto(db.Entity):
    _table_ = "reparto"

    id_cassa = Required(str, 100)
    id_reparto = Required(str, 100)
    id_negozio = Required(str, 100)
    id_cliente = Required(str, 100)
    nome = Optional(str)
    presenza = Required(int)
    incasso = Required(float)
    PrimaryKey(id_cassa, id_reparto, id_negozio, id_cliente)