import datetime
from cliente import Cliente

class Solicitacao():
    descricao: str
    dataEnvio: datetime
    dataRecebimento: datetime
    dataVisto: datetime
    tipo:int
    
    def __init__(self,descricao,tipo):
        self.descricao = descricao
        self.tipo = tipo
        
    def notificaPersonal(cliente: Cliente):
        ...