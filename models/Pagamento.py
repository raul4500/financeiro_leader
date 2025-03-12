from database import db
from sqlalchemy import*
from sqlalchemy.orm import*


class Pagamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reserva_id = db.Column(db.Integer, db.ForeignKey('reserva.id'), nullable=False)
    data_pagamento = db.Column(db.Date, nullable=False)
    valor = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)  # Ex: 'pendente', 'pago'

    def __repr__(self):
        return f"<Pagamento {self.status} de {self.valor} para Reserva {self.reserva_id}>"

    def toJson(self):
        return {
            "id": self.id,
            "reserva_id": self.reserva_id,
            "data_pagamento": self.data_pagamento.strftime('%Y-%m-%d %H:%M:%S'),
            "valor": self.valor,
            "status": self.status
        }