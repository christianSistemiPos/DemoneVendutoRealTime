from enum import Enum
from datetime import datetime
import uuid 
class CodiceAnomalia(Enum):
    Fidelity = "Fidelity"
    Abort = "Abort"
    Storno = "Storno"
    Reso = "Reso"
    ResoScontrino = "Reso da scontrino"

class TipoAnomalia():
    """
        Dizionario per i vari tipi di Anomalia
    """
    FidelityLimite = lambda nr_fidelity, nr_volte_in_cassa: f'{nr_fidelity};{nr_volte_in_cassa}'
    
    Abort = lambda ora_anomalia, operatore, nr_scontrino, totale: f'Abort per lo scontrino numero: {nr_scontrino}, del valore di {totale} euro.'
    
    Storno = lambda ora_anomalia, operatore, descrizione, ean, valore: f'Storno per articolo: {descrizione}, ean: {ean}, {valore} euro.'
    
    Reso = lambda scontrino,ora_anomalia, operatore, descrizione, ean, valore: f"Reso per articolo {descrizione}, ean: {ean}, {valore} euro."
    
    ResoScontrino = lambda scontrino,ora_anomalia, operatore, descrizione, ean, valore: f"Reso da scontrino {scontrino}, per articolo {descrizione}, ean: {ean}, {valore}."

class Anomalia:
    """
        Modello per la gestione anomalia
    """
    
    def __init__(self, tipo_anomalia: str, ora_anomalia: datetime, operatore: str, descrizione_anomalia: str):
        """Costruttore classe anomalia

        Args:
            ora_anomalia (datetime): 
                Orario in cui l'anomalia e` sopraggiunta
            operatore (str): 
                Operatore che ha innescato l'anomalia
            descrizione_anomalia (str): 
                Descrizione dell'anomalia avvenuta
        """
        self.tipo_anomalia = tipo_anomalia
        self.ora_anomalia = ora_anomalia
        self.operatore = operatore
        self.descrizione_anomalia = descrizione_anomalia
        
        
        
        