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
        self.dataEnvio = datetime.now() #registra a criacao/envio da solicitacao
        
    def notificaPersonal(cliente: Cliente):
        ...