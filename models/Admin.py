from database import db
from sqlalchemy import*
from sqlalchemy.orm import*

# Classe Admin
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Admin {self.nome}>"

    def toJson(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
        }
