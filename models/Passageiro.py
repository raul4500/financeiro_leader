from database import db
from sqlalchemy import*
from sqlalchemy.orm import*
from datetime import datetime

# Classe Passageiro
class Passageiro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    nascimento = db.Column(db.Date, nullable=False)
    rg = db.Column(db.String(9), unique=True, nullable=False)
    telefone = db.Column(db.String(11), nullable=False)
    # Relacionamento: Um Passageiro pode ter várias reservas
    reservas = db.relationship('Reserva', backref='passageiro', lazy=True)

    def __repr__(self):
        return f"<Passageiro {self.nome}>"

    def toJson(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "nascimento": self.nascimento,
            "rg": self.rg,
            "telefone": self.telefone,
            "reservas": [reserva.toJson() for reserva in self.reservas]
        }
