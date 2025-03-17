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
    def addPassageiro(nome, nascimento, rg, telefone):
        passageiro = Passageiro(nome=nome, nascimento=nascimento, rg=rg, telefone=telefone)
        db.session.add(passageiro)
        db.session.commit()
        return passageiro.toJson()

    @staticmethod
    def attPassageiro(nome, nascimento, rg, telefone):
        Passageiro = PassageiroDao.getPassageiroByRg(rg)
        if Passageiro:
            Passageiro.nome = nome
            Passageiro.nascimento = nascimento
            Passageiro.rg = rg
            Passageiro.telefone = telefone
            db.session.commit()
        return Passageiro.toJson()

    @staticmethod
    def delPassageiro(id):
        Passageiro = PassageiroDao.getPassageiro(id)
        if Passageiro:
            db.session.delete(Passageiro)
            db.session.commit()