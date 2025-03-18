from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask import session as cookies_session
from database import*
from repository.__init__ import*
from datetime import*

lembrete_controller = Blueprint('lembrete_controller', __name__)

lembreteRepository = LembreteRepository()

@lembrete_controller.route('/add_lembrete', methods=["POST"])
def index():
    mensagem = request.form['mensagem']
    if mensagem:
       lembreteRepository.createLembrete(mensagem)
    return redirect(url_for('index_controller.index'))

@lembrete_controller.route('/deletar_lembrete/<int:id>')
def deletarLembrete(id):
    if lembreteRepository.getLembrete(id):
        lembreteRepository.deleteLembrete(id)
    return redirect(url_for('index_controller.index'))