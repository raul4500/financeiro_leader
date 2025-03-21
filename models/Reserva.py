from database import db
from sqlalchemy import*
from sqlalchemy.orm import*
from datetime import datetime

class Reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    assento = db.Column(db.Integer, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('passageiro.id'), nullable=True)
    viagem_id = db.Column(db.Integer, db.ForeignKey('viagem.id'), nullable=True)
    # Relacionamento: Cada reserva tem um pagamento (1:1)

    def __repr__(self):
        return f"<{self.viagem_id}>"

    def toJson(self):
        return {
            "id": self.id,
            "cliente_id": self.cliente_id,
            "viagem_id": self.viagem_id,
            "pagamento": self.pagamento.toJson() if self.pagamento else None
        }

