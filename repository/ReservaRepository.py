from dao.__init__ import *

class ReservaRepository:
    def __init__(self):
        self.reservaDao = ReservaDao()

    def getAllReservas(self):
        return self.reservaDao.getAllReservas()

    def getReserva(self, id):
        return self.reservaDao.getReserva(id)

    def createReserva(self, cliente_id, viagem_id):
        return self.reservaDao.addReserva(cliente_id, viagem_id)

    def updateReserva(self, id, cliente_id, viagem_id):
        return self.reservaDao.attReserva(id, cliente_id, viagem_id)

    def deleteReserva(self, id):
        return self.reservaDao.delReserva(id)