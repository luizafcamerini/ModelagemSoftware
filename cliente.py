from solicitacao import Solicitacao
from personal import Personal
from treino import Treino
from sessao import Sessao
from programa import Programa

class Cliente():
    nome:str
    sobrenome:str
    id: int # o id pode ser gerado automaticamente, tipo uma hash a partir do nome?
    personal: Personal
    sessoes:list
    programas: list
    
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        # cria o id como uma hash
        # adiciona ele na base de dados
        self.__registraClienteBanco(self)
    
    def __registraClienteBanco(self):
        #inclui o cliente no banco de dados
        ...
    
    def getPersonal(self):
        return self.personal
    
    def getId(self):
        return self.id

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
    
    