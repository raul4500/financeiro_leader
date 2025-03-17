from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask import session as cookies_session
from database import*
from repository.__init__ import*
from datetime import*

index_controller = Blueprint('index_controller', __name__)

viagemRepository = ViagemRepository()
passageiroRepository = PassageiroRepository()
lembreteRepository = LembreteRepository()

@index_controller.route('/')
def index():
    viagens = viagemRepository.getAllViagens()
    passageiros = passageiroRepository.getAllPassageiros()
    lembretes = lembreteRepository.getAllLembretes()
    return render_template('index.html', viagens=viagens, passageiros=passageiros, lembretes=lembretes)
