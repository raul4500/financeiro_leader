from dao.__init__ import *

class PassageiroRepository:
    def __init__(self):
        self.passageiroDao = PassageiroDao()

    def getAllPassageiros(self):
        return self.passageiroDao.getAllPassageiros()

    def getPassageiro(self, id):
        return self.passageiroDao.getPassageiro(id)
    
    def getPassageiroByRg(self, rg):
        return self.passageiroDao.getPassageiroByRg(rg)

    def createPassageiro(self, nome, nascimento, rg, telefone):
        return self.passageiroDao.addPassageiro(nome, nascimento, rg, telefone)

    def updatePassageiro(self, nome, nascimento, rg, telefone):
        return self.passageiroDao.attPassageiro(nome, nascimento, rg, telefone)

    def deletePassageiro(self, id):
        return self.passageiroDao.delPassageiro(id)