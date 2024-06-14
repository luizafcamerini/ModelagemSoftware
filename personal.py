from cliente import Cliente
import datetime
from programa import Programa
from treino import Treino

class Personal():
    nome: str
    sobrenome: str
    id: int
    clientesAssociados: list
    
    def __init__(self) -> None:
        pass

    def pesquisaCliente(self, idCliente, nomeCliente, sobrenomeCliente) -> list:
        if idCliente != None:
            #procura o cliente na base de dados
            ...
        elif nomeCliente != None:
            #procura o cliente na base de dados
            ...
        else:
            #procura o cliente na base de dados
            ...
        #return lista de clientes (pode ter um cliente apenas)
    
    def pesquisaSolicitacao(self, cliente:Cliente, dataEnvio: datetime):
        #pesquisa solicitacao na base de dados
        ...
    
    def criaPrograma(self,cliente:Cliente, estimativaTempo, treinos:list):
        ...
        
    def registraCliente(self, nomeCliente:str, sobrenomeCliente:str)->bool:
        cliente = Cliente(nomeCliente, sobrenomeCliente)
        verificacao = self.__verificaExisteCliente(nomeCliente, sobrenomeCliente)
    
    def __verificaExisteCliente(self, nomeCliente, sobrenomeCliente)->bool:
        #verifica se aquele cliente ja existe no banco de clientes
        ...
    
    def __pesquisarSolicitacoesPendentes():
        ...
    
    def __pesquisarTreino(diaSemana, data):
        ...
    
    def __registraTreino(programa:Programa, treino:Treino):
        ...
        