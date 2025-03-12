from models.__init__ import *

# classe dos autores com suas próprias funções (CRUD)

class AdminDao:
    @staticmethod
    def getAdmin(id):
        return Admin.query.get(id)
    
    @staticmethod
    def getAdminByEmail(email):
        return Admin.query.filter_by(email=email).first()
    
    @staticmethod
    def getAllAdmins():
        return Admin.query.all()
    
    @staticmethod
    def addAdmin(nome, email, senha):
        admin = Admin(nome=nome, email=email, senha=senha)
        db.session.add(admin)
        db.session.commit()
        return admin.toJson()
    
    @staticmethod
    def attAdmin(id, nome, email, senha):
        admin = AdminDao.getAdmin(id)
        if admin:
            admin.nome = nome
            admin.email = email
            admin.senha = senha
            db.session.commit()
        return admin.toJson()
    
    @staticmethod
    def delAdmin(id):
        admin = AdminDao.getAdmin(id)
        if admin:
            db.session.delete(admin)
            db.session.commit()
        return admin.toJson()