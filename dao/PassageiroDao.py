from models.__init__ import *

# classe dos autores com suas próprias funções (CRUD)

class PassageiroDao:
    @staticmethod
    def getPassageiro(id):
        return Passageiro.query.get(id)
    
    @staticmethod
    def getPassageiroByEmail(email):
        return Passageiro.query.filter_by(email=email).first()
    
    @staticmethod
    def getPassageiroByRg(rg):
        return Passageiro.query.filter_by(rg=rg).first()

    @staticmethod
    def getAllPassageiros():
        return Passageiro.query.all()

    @staticmethod
    def addPassageiro(nome, email, nascimento, rg, telefone):
        Passageiro = Passageiro(nome=nome, email=email, nascimento=nascimento, rg=rg, telefone=telefone)
        db.session.add(Passageiro)
        db.session.commit()
        return Passageiro.toJson()

    @staticmethod
    def attPassageiro(email, nome, novo_email, nascimento, rg, telefone):
        Passageiro = PassageiroDao.getPassageiroByEmail(email)
        if Passageiro:
            Passageiro.nome = nome
            Passageiro.email = novo_email
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