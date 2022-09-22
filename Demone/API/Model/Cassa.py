
from typing import List
from .Reparto import Reparto
from .Pagamento import Pagamento
import logging

class Cassa:
    """
        Modello di rappresentazione di una cassa
    """

    def __init__(self, id_cassa: str, numero_scontrini: int = 0, numero_scontrini_fidelity: int = 0, totale: float = 0.0,
                 incasso_per_reparti: List[Reparto] = [],
                 incasso_per_tipo_pagamento: List[Pagamento] = []):
        """
        Costruttore Cassa

        Parameters
        ----------
        id_cassa : str
            Identificativo cassa

        numero_scontrini : int
            Numero che indica quanti scontrini sono stati emessi

        numero_scontrini_fidelity : int
            Indica il totale degli scontrini fidelity emessi

        totale: float
            Indica l'incasso totale della cassa

        incasso_per_reparti: List[Reparto]
            Colleziona gli incassi relativi ad ogni reparto, per cassa.

        incasso_per_tipo_pagamento: List[Pagamento]
            Colleziona gli incassi relativi ad ogni tipologia di pagamento, per cassa.

        Raises
        ---------
        TypeError
            Id cassa non valido
        ValueError
            Gli scontrini non hanno referenza (None)
        """
        
        logging.info("Cassa: Creazione cassa...")
        self.id_cassa = id_cassa
        
        self.numero_scontrini = numero_scontrini

        self.numero_scontrini_fidelity = numero_scontrini_fidelity

        self.totale = totale

        self.incasso_per_reparto = incasso_per_reparti

        self.incasso_per_tipo_pagamento = incasso_per_tipo_pagamento

        logging.info(f"Cassa: Id cassa: {self.id_cassa}")
        logging.info(f"Cassa: Numero Scontrini: {self.numero_scontrini}")
        logging.info(f"Cassa: Numero Scontrini Fidelity: {self.numero_scontrini_fidelity}")
        logging.info(f"Cassa: Importo Totale: {self.totale} euro")
        logging.info(f"Cassa: Incasso per reparto: {self.incasso_per_reparto}")
        logging.info(f"Cassa: Incasso per tipo pagamento: {self.incasso_per_tipo_pagamento}")
    
    
        logging.info("Cassa: Ok.")

    def __repr__(self):
        return f"Cassa: {self.id_cassa}, Scontrini: {self.numero_scontrini}"
