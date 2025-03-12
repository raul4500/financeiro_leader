from dao.__init__ import *

class ViagemRepository:
    def __init__(self):
        self.viagemDao = ViagemDao()

    def getAllViagens(self):
        return self.viagemDao.getAllViagens()

    def getViagem(self, id):
        return self.viagemDao.getViagem(id)
    
    def getViagemByMonth(self, month):
        return self.viagemDao.getViagensInMonth(month)
    
    def getViagemByDestination(self, destination):
        return self.viagemDao.getViagemByDestination(destination)
    
    def getViagemByDestinationAndMonth(self, destination, month):
        return self.viagemDao.getViagemByDestinationAndMonth(destination, month)
    
    def createViagem(self, destino, data_inicio, data_fim, preco, qtd_assentos, assentos_indisponiveis, imagem_url, descricao, inclusos):
        return self.viagemDao.addViagem(destino, data_inicio, data_fim, preco, qtd_assentos, assentos_indisponiveis, imagem_url, descricao, inclusos)

    def updateViagem(self, id, destino, data_inicio, data_fim, preco, qtd_assentos, assentos_indisponiveis, imagem_url, descricao, inclusos):
        return self.viagemDao.attViagem(id, destino, data_inicio, data_fim, preco, qtd_assentos, assentos_indisponiveis, imagem_url, descricao, inclusos)

    def deleteViagem(self, id):
        return self.viagemDao.delViagem(id)
