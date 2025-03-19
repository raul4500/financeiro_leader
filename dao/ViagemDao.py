from models import Viagem, db
from sqlalchemy import extract
from datetime import datetime

class ViagemDao:
    @staticmethod
    def getViagem(id):
        return Viagem.query.get(id)

    @staticmethod
    def getAllViagens():
        return Viagem.query.all()
    
    @staticmethod
    def getViagensInMonth(month):
        return Viagem.query.filter(
            extract('month', Viagem.data_inicio) == month
        ).all()
    
    @staticmethod
    def getViagemByDestination(destination):
        return Viagem.query.filter_by(destino=destination).all()
    
    @staticmethod
    def getViagemByDestinationAndMonth(destination, month):
        return Viagem.query.filter(
            extract('month', Viagem.data_inicio) == month,
            Viagem.destino == destination
        ).all()

    @staticmethod
    def addViagem(destino, data_inicio, data_fim, preco, qtd_assentos, assentos_indisponiveis, tipo_onibus, descricao, inclusos):
        viagem = Viagem(destino=destino, data_inicio=data_inicio, data_fim=data_fim, preco=preco, qtd_assentos=qtd_assentos, assentos_indisponiveis=assentos_indisponiveis, tipo_onibus=tipo_onibus, descricao=descricao, inclusos=inclusos)
        db.session.add(viagem)
        db.session.commit()
        return viagem.toJson()

    @staticmethod
    def attViagem(id, destino, data_inicio, data_fim, preco, qtd_assentos, assentos_indisponiveis, tipo_onibus, descricao, inclusos):
        viagem = ViagemDao.getViagem(id)
        if viagem:
            viagem.destino = destino
            viagem.data_inicio = data_inicio
            viagem.data_fim = data_fim
            viagem.preco = preco
            viagem.aqt_assentos = qtd_assentos
            viagem.assentos_indisponiveis = assentos_indisponiveis
            viagem.tipo_onibus = tipo_onibus
            viagem.descricao = descricao
            viagem.inclusos = inclusos
            db.session.commit()
        return viagem.toJson()

    @staticmethod
    def delViagem(id):
        viagem = ViagemDao.getViagem(id)
        if viagem:
            db.session.delete(viagem)
            db.session.commit()
        return viagem.toJson()
