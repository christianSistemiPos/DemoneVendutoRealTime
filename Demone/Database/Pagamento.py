from pony.orm import *
from Database import db


class TablePagamento(db.Entity):
    _table_ = "pagamento"

    id_cassa = Required(str, 100)
    id_negozio = Required(str, 100)
    id_cliente =Required(str, 100)
    tipo_pagamento = Required(str)
    incasso = Required(float, default=0)
    PrimaryKey(id_cassa, id_negozio, id_cliente,tipo_pagamento)