from dao.__init__ import *

class PagamentoRepository:
    def __init__(self):
        self.pagamentoDao = PagamentoDao()

    def getAllPagamentos(self):
        return self.pagamentoDao.getAllPagamentos()

    def getPagamento(self, id):
        return self.pagamentoDao.getPagamento(id)

    def createPagamento(self, reserva_id, data_pagamento, valor, status):
        return self.pagamentoDao.addPagamento(reserva_id, data_pagamento, valor, status)

    def updatePagamento(self, id, reserva_id, data_pagamento, valor, status):
        return self.pagamentoDao.attCliente(id, reserva_id, data_pagamento, valor, status)

    def deletePagamento(self, id):
        return self.pagamentoDao.delPagamento(id)
