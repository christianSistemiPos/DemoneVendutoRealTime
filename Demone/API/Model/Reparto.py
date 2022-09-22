import logging

class Reparto:
    """
        Classe rappresentazione reparto
    """
    def __init__(self, nome: str, codice: str, incasso: float, presenza: int):
        """
            Costruttore per classe reparto

        Parameters
        ----------
        nome : str
            Nome del reparto
        codice : str
            Codice del reparto
        incasso : float
            Incasso totale del reparto
        presenza : int
            Numero di articoli del reparto presenti in tutti gli scontrini.
        """
        
        logging.info("Pagamento: Chiamato costruttore per reparto.")

        self.nome = nome
        self.codice = codice
        self.incasso = incasso
        self.presenza = presenza
        
        logging.info(f"Reparto: Nome: {self.nome}")
        logging.info(f"Reparto: Codice: {self.codice}")
        logging.info(f"Reparto: Presenze: {self.presenza}")
        logging.info(f"Reparto: Importo: {self.incasso} euro")
        logging.info("Reparto: Ok.")

    def __repr__(self):
        return f"Reparto: {self.nome}, codice: {self.codice}, incasso: {self.incasso}"
