from usuario import Usuario
from solicitacao import Solicitacao
from personal import Personal
from treino import Treino
from sessao import Sessao
from programa import Programa

class Cliente(Usuario):
    personal: Personal
    sessoes:list
    programas: list
    
    def __init__(self, nome: str, sobrenome: str, id: int) -> None:
        id = self.__generate_id(nome, sobrenome)
        super().__init__(id, nome, sobrenome)
        self.personal = None
        self.sessoes = []
        self.programas = []
        # cria o id como uma hash
        # adiciona ele na base de dados
        self.__registraClienteBanco()
    
    def __registraClienteBanco(self):
        #inclui o cliente no banco de dados
        ...
    
    def getPersonal(self) -> Personal:
        return self.personal

    def setProgramas(self, programas:list):
        self.programas = programas
        
    def __realizaSolicitacao(self, descricao, tipo):
        solicitacao = Solicitacao(descricao)
        ...
    
    def criaSessao(self):
        self.sessoes.append(Sessao())
    
    def acessaPrograma(self, programaID):
        ...
    
    def terminaTreino(self, treino: Treino):
        ...
    
    def registraExercicio(self, exercicio):
        ...
        
    def solicitaPrograma(self):
        ...
    
    def solicitaModificacaoExercicio(self):
        ...
