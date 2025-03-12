from models.__init__ import *

# classe dos autores com suas próprias funções (CRUD)

class ClienteDao:
    @staticmethod
    def getCliente(id):
        return Cliente.query.get(id)
    
    
    @staticmethod
    def getClienteByEmail(email):
        return Cliente.query.filter_by(email=email).first()
    
    @staticmethod
    def getClienteByRg(rg):
        return Cliente.query.filter_by(rg=rg).first()

    @staticmethod
    def getAllClientes():
        return Cliente.query.all()

    @staticmethod
    def addCliente(nome, email, nascimento, rg, telefone, senha):
        cliente = Cliente(nome=nome, email=email, nascimento=nascimento, rg=rg, telefone=telefone, senha=senha)
        db.session.add(cliente)
        db.session.commit()
        return cliente.toJson()

    @staticmethod
    def attCliente(email, nome, novo_email, nascimento, rg, telefone):
        cliente = ClienteDao.getClienteByEmail(email)
        if cliente:
            cliente.nome = nome
            cliente.email = novo_email
            cliente.nascimento = nascimento
            cliente.rg = rg
            cliente.telefone = telefone
            db.session.commit()
        return cliente.toJson()

    @staticmethod
    def delCliente(id):
        cliente = ClienteDao.getCliente(id)
        if cliente:
            db.session.delete(cliente)
            db.session.commit()