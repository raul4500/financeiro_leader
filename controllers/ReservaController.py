from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask import session as cookies_session
from database import*
from repository.__init__ import*
from datetime import*

reserva_controller = Blueprint('reserva_controller', __name__)

reservaRepository = ReservaRepository()
viagemRepository = ViagemRepository()

@reserva_controller.route('/reservar/<int:id>', methods=['GET'])
def index(id):
    usuario = cookies_session.get('usuario_email')
    viagem = viagemRepository.getViagem(id)
    return render_template('reservar.html', usuario=usuario, viagem=viagem)