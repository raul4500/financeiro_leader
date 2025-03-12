from dao.__init__ import *

class AdminRepository:
    def __init__(self):
        self.adminDao = AdminDao()
    
    def getAllAdmins(self):
        return self.adminDao.getAllAdmins()
    
    def getAdmin(self, id):
        return self.adminDao.getAdmin(id)
    
    def getAdminByEmail(self, email):  
        return self.adminDao.getAdminByEmail(email)
    
    def createAdmin(self, nome, email, senha):
        return self.adminDao.addAdmin(nome, email, senha)
    
    def updateAdmin(self, id, nome, email, senha):
        return self.adminDao.attAdmin(id, nome, email, senha)
    
    def deleteAdmin(self, id):
        return self.adminDao.delAdmin(id)