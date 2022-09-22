from pony.orm import *
from Database import db


class TableCassa(db.Entity):
    _table_ = "cassa"

    id_cassa = Required(str, 100)
    id_negozio = Required(str, 100)
    id_cliente = Required(str, 100)
    numero_scontrini = Required(int, default=0)
    numero_scontrini_fidelity = Required(int, default=0)
    totale = Required(float, default=0)
    PrimaryKey(id_cassa, id_negozio, id_cliente)


    

