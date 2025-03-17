from database import db
from sqlalchemy import*
from sqlalchemy.orm import*

# Classe Lembrete
class Lembrete(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mensagem = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<Lembrete {self.mensagem}>"

    def toJson(self):
        return {
            "id": self.id,
            "mensagem": self.mensagem
        }
