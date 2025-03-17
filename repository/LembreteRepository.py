from dao.__init__ import *

class LembreteRepository:
    def __init__(self):
        self.lembreteDao = LembreteDao()

    def getAllLembretes(self):
        return self.lembreteDao.getAllLembretes()

    def getLembrete(self, id):
        return self.lembreteDao.getLembrete(id)

    def createLembrete(self, mensagem):
        return self.lembreteDao.addLembrete(mensagem)

    def updateLembrete(self, id, mensagem):
        return self.lembreteDao.attLembrete(id, mensagem)

    def deleteLembrete(self, id):
        return self.lembreteDao.delLembrete(id)