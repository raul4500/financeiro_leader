from database import db
from sqlalchemy import*
from sqlalchemy.orm import*
from datetime import datetime

class Reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=True)
    viagem_id = db.Column(db.Integer, db.ForeignKey('viagem.id'), nullable=True)
    # Relacionamento: Cada reserva tem um pagamento (1:1)
    pagamento = db.relationship('Pagamento', backref='reserva', uselist=False)

    def __repr__(self):
        return f"<Reserva Cliente {self.cliente_id} para {self.viagem_id}>"

    def toJson(self):
        return {
            "id": self.id,
            "cliente_id": self.cliente_id,
            "viagem_id": self.viagem_id,
            "pagamento": self.pagamento.toJson() if self.pagamento else None
        }

