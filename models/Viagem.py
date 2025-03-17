from database import db
from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship

class Viagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destino = db.Column(db.String(100), nullable=False)
    data_inicio = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    qtd_assentos = db.Column(db.Integer, nullable=False)
    assentos_indisponiveis = db.Column(db.Integer, nullable=True)
    descricao = db.Column(db.String(400), nullable=False)
    inclusos = db.Column(db.String(400), nullable=False)
    # Relacionamento: Uma viagem pode ter várias reservas
    reservas = db.relationship('Reserva', backref='viagem', lazy=True)

    def __repr__(self):
        return f"<Viagem {self.destino}>"

    def toJson(self):
        return {
            "id": self.id,
            "destino": self.destino,
            "data_inicio": self.data_inicio.strftime('%Y-%m-%d'),
            "data_fim": self.data_fim.strftime('%Y-%m-%d'),
            "preco": self.preco,
            "qtd_assentos": self.qtd_assentos,
            "assentos_indisponiveis": self.assentos_indisponiveis,
            "descricao": self.descricao,
            "inclusos": self.inclusos,
            "reservas": [reserva.toJson() for reserva in self.reservas]
        }