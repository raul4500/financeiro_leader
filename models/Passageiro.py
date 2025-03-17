from database import db
from sqlalchemy import*
from sqlalchemy.orm import*
from datetime import datetime

# Classe Passageiro
class Passageiro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    nascimento = db.Column(db.Date, nullable=True)
    rg = db.Column(db.String(9), unique=True, nullable=False)
    telefone = db.Column(db.String(11), nullable=False)
    # Relacionamento: Um Passageiro pode ter várias reservas

    def __repr__(self):
        return f"<Passageiro {self.nome}>"

    def toJson(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "nascimento": self.nascimento,
            "rg": self.rg,
            "telefone": self.telefone,
            #"reservas": [reserva.toJson() for reserva in self.reservas]
        }
