
from typing import List
from .Cassa import Cassa
import logging


class Negozio:
    """
        Classe Modello per definizione Negozio
    """

    def __init__(self, id_negozio:str, id_cliente: str, nome_negozio: str, casse: List[Cassa] = None, chiuso: bool = False):
        """
        Costruttore Negozio

        Parameters
        ----------
        id_negozio : str
            Id del negozio per sistemipos

        id_cliente : str
            Id del cliente

        nome_negozio : str
            Nome del negozio.

        casse : List[Cassa], optional
            Le casse associate al negozio.

        chiuso : bool, optional
            Indica se il negozio è chiuso (True) o aperto (False)
        Raises
        ---------
        ValueError
            Il campo _negozio_ è una stringa vuota

        """
        logging.info("Negozio: Chiamato costruttore negozio.")
        logging.info("Negozio: Lettura dati..")
        if id_negozio == "":
            logging.error("Negozio: Id negozio non valorizzato")
            raise ValueError("Campo id negozio vuoto")
        self.id_negozio = id_negozio

        if id_cliente == "":
            logging.error("Negozio: Id negozio non valorizzato")
            raise ValueError("Campo id negozio vuoto")
        self.id_cliente = id_cliente
        
        if nome_negozio == "":
            logging.error("Negozio: Nome negozio non valorizzato")
            raise ValueError("Campo nome negozio vuoto")
        self.nome_negozio = nome_negozio
        
        logging.info("Negozio: Analisi casse..")
        if not casse or len(casse) == 0:
            logging.info(f"Negozio: Nessuna cassa valorizzata per il punto vendita {self.nome_negozio}")
            return
        
        self.casse = casse

        logging.info("Negozio: Chisura..")
        self.chiuso = chiuso

        logging.info("Negozio: Fine.")

    def __repr__(self):
        return f"Negozio: {self.nome_negozio}"
