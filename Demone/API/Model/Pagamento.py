import logging

class Pagamento:
    """
    Classe per rappresentazione pagamento di uno scontrino
    """

    def __init__(self, tipo_pagamento: str = None, incasso: float = 0.0):
        """
        Costruttore classe pagamento

        Parameters
        ----------
        tipo_pagamento
            Tipologia del pagamento, Bancomat, CONTANTE..

        incasso
            Importo del pagamento
        """
        logging.info("Pagamento: Chiamato costruttore..")
        self.tipo_pagamento = tipo_pagamento
        self.incasso = incasso
        logging.info(f"Pagamento: Tipo Pagamento: {self.tipo_pagamento}")
        logging.info(f"Pagamento: Importo: {self.incasso} euro")
        logging.info("Pagamento: Ok.")

    def __repr__(self):
        return f"Pagamento: {self.tipo_pagamento}, incasso: {self.incasso}"