from solicitacao import Solicitacao
from personal import Personal
from treino import Treino
from sessao import Sessao

class Cliente():
    nome:str
    sobrenome:str
    id: int # o id pode ser gerado automaticamente, tipo uma hash a partir do nome?
    personal: Personal
    sessoes:list
    
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def getPersonal(self):
        return self.personal
    
    def getId(self):
        return self.id
        
    def realizaSolicitacao(self, descricao, tipo):
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
    
    