from dao.__init__ import *

class ClienteRepository:
    def __init__(self):
        self.clienteDao = ClienteDao()

    def getAllClientes(self):
        return self.clienteDao.getAllClientes()

    def getCliente(self, id):
        return self.clienteDao.getCliente(id)
    
    def getClienteByEmail(self, email):
        return self.clienteDao.getClienteByEmail(email)
    
    def getClienteByRg(self, rg):
        return self.clienteDao.getClienteByRg(rg)

    def createCliente(self, nome, email, nascimento, rg, telefone, senha):
        return self.clienteDao.addCliente(nome, email, nascimento, rg, telefone, senha)

    def updateCliente(self, email, nome, novo_email, nascimento, rg, telefone):
        return self.clienteDao.attCliente(email, nome, novo_email, nascimento, rg, telefone)

    def deleteCliente(self, id):
        return self.clienteDao.delCliente(id)