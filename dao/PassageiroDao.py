from models.__init__ import *

# classe dos autores com suas próprias funções (CRUD)

class PassageiroDao:
    @staticmethod
    def getPassageiro(id):
        return Passageiro.query.get(id)
    
    @staticmethod
    def getPassageiroByRg(rg):
        return Passageiro.query.filter_by(rg=rg).first()

    @staticmethod
    def getAllPassageiros():
        return Passageiro.query.all()

    @staticmethod
    def addPassageiro(nome, nascimento, rg, telefone, status):
        passageiro = Passageiro(nome=nome, nascimento=nascimento, rg=rg, telefone=telefone, status=status)
        db.session.add(passageiro)
        db.session.commit()
        return passageiro.toJson()

    @staticmethod
    def attPassageiro(nome, nascimento, rg, telefone, status):
        passageiro = PassageiroDao.getPassageiroByRg(rg)
        if passageiro:
            passageiro.nome = nome
            passageiro.nascimento = nascimento
            passageiro.rg = rg
            passageiro.telefone = telefone
            passageiro.status = status
            db.session.commit()
        return passageiro.toJson()

    @staticmethod
    def attStatus(rg, status):
        passageiro = PassageiroDao.getPassageiroByRg(rg)
        if passageiro:
            passageiro.status = status
            db.session.commit()
        return passageiro.toJson()

    @staticmethod
    def delPassageiro(id):
        passageiro = PassageiroDao.getPassageiro(id)
        if passageiro:
            db.session.delete(passageiro)
            db.session.commit()