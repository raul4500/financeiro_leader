from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask import session as cookies_session
from database import*
from repository.__init__ import*
from datetime import*

reserva_controller = Blueprint('reserva_controller', __name__)

reservaRepository = ReservaRepository()
viagemRepository = ViagemRepository()
passageiroRepository = PassageiroRepository()

@reserva_controller.route('/reservar/<int:viagem_id>/<int:passageiro_id>', methods=['GET', 'POST'])
def index(viagem_id, passageiro_id):
    passageiro = passageiroRepository.getPassageiro(passageiro_id)
    viagem = viagemRepository.getViagem(viagem_id)
    if passageiro and viagem:
        reservaRepository.createReserva(passageiro_id, viagem_id)
    return redirect(url_for('viagem_controller.teste'))