# from solicitacao import Solicitacao
import hashlib

class Usuario():
    nome:str
    sobrenome:str
    id: int # o id pode ser gerado automaticamente, tipo uma hash a partir do nome?
    
    def __init__(self, id, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def __generate_id(self, nome: str, sobrenome: str) -> int:
        return int(hashlib.sha256(f"{nome}{sobrenome}".encode()).hexdigest(), 16) % 10**8

    def getId(self) -> int:
        return self.id

    def getNome(self) -> str:
        return self.nome
    
    def getSobrenome(self) -> str:
        return self.sobrenome


        
    
    
    