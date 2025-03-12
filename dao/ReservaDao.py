from models.__init__ import*

class ReservaDao:
    @staticmethod
    def getReserva(id):
        return Reserva.query.get(id)

    @staticmethod
    def getAllReservas():
        return Reserva.query.all()

    @staticmethod
    def addReserva(cliente_id, viagem_id):
        reserva = Reserva(cliente_id=cliente_id, viagem_id=viagem_id)
        db.session.add(reserva)
        db.session.commit()
        return reserva.toJson()

    @staticmethod
    def attReserva(id, cliente_id, viagem_id):
        reserva = ReservaDao.getReserva(id)
        if reserva:
            reserva.cliente_id = cliente_id
            reserva.viagem_id = viagem_id
            db.session.commit()
        return reserva.toJson()

    @staticmethod
    def delReserva(id):
        reserva = ReservaDao.getReserva(id)
        if reserva:
            db.session.delete(reserva)
            db.session.commit()
        return reserva.toJson()