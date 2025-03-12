from models.__init__ import *

class PagamentoDao:
    @staticmethod
    def getPagamento(id):
        return Pagamento.query.get(id)

    @staticmethod
    def getAllPagamentos():
        return Pagamento.query.all()

    @staticmethod
    def addPagamento(reserva_id, data_pagamento, valor, status):
        pagamento = Pagamento(reserva_id=reserva_id, data_pagamento=data_pagamento, valor=valor, status=status)
        db.session.add(pagamento)
        db.session.commit()
        return pagamento.toJson()

    @staticmethod
    def attPagamento(id, valor, status):
        pagamento = PagamentoDao.getPagamento(id)
        if pagamento:
            pagamento.valor = valor
            pagamento.status = status
            db.session.commit()
        return pagamento.toJson()

    @staticmethod
    def delPagamento(id):
        pagamento = PagamentoDao.getPagamento(id)
        if pagamento:
            db.session.delete(pagamento)
            db.session.commit()
        return pagamento.toJson()