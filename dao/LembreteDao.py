from models.__init__ import *

class LembreteDao:
    @staticmethod
    def getLembrete(id):
        return Lembrete.query.get(id)

    @staticmethod
    def getAllLembretes():
        return Lembrete.query.all()

    @staticmethod
    def addLembrete(mensagem):
        lembrete = Lembrete(mensagem=mensagem)
        db.session.add(lembrete)
        db.session.commit()
        return lembrete.toJson()

    @staticmethod
    def attLembrete(id, mensagem):
        lembrete = LembreteDao.getLembrete(id)
        if lembrete:
            lembrete.mensagem = mensagem
            db.session.commit()
        return lembrete.toJson()

    @staticmethod
    def delLembrete(id):
        lembrete = LembreteDao.getLembrete(id)
        if lembrete:
            db.session.delete(lembrete)
            db.session.commit()
        return lembrete.toJson()