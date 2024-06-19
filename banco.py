from pymongo import *

class Banco():
  __instance = None

  def __new__(cls):
      if Banco.__instance is None:
        Banco.__instance = super().__new__(cls)
      return Banco.__instance
  
  def __init__(self):
    self.m_cliente = MongoClient("localhost", 27017, serverSelectionTimeoutMS=3000)
    self.bd = self.m_cliente["banco"]
    self.clientes = self.bd["clientes"]
    self.personais = self.bd["personais"]
    self.exercicios = self.bd["exercicios"]
    self.sessoes = self.bd["sessoes"]
    #self.personais.insert_one({"nome": "Maria", "sobrenome": "da Silva", "matricula": "00000", "senha": "12345678"})
     
  def get_instance():
    if Banco.__instance is None:
        Banco.__instance = Banco()
    return Banco.__instance
  
  def get_database(self):
     return self.bd