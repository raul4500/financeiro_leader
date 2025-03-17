from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask import session as cookies_session
from database import*
from repository.__init__ import*
from datetime import*

admin_controller = Blueprint('admin_controller', __name__)

adminRepository = AdminRepository()
viagemRepository = ViagemRepository()
clienteRepository = PassageiroRepository()

@admin_controller.route('/gerenciar', methods=['GET'])
def index():
    if cookies_session['usuario_email'] == 'admin@gmail.com':
        viagens = viagemRepository.getAllViagens()
        clientes = clienteRepository.getAllClientes()
        return render_template('gerenciar.html', viagens=viagens, clientes=clientes)
    print('somente administradores podem ter acesso a esta página')
    return redirect(url_for('viagem_controller.index'))

@admin_controller.route('/cadastrar_viagem', methods=['GET', 'POST'])
def cadastrar_viagem():
    if cookies_session['usuario_email']:
        if request.method == 'POST':
            destino = request.form['destino']
            data_inicio = request.form['data_inicio']
            data_fim = request.form['data_fim']
            preco = request.form['preco']
            qtd_assentos = request.form['qtd_assentos']
            assentos_indisponiveis = None
            imagem_url = request.form['imagem_url']
            descricao = request.form['descricao']
            inclusos = request.form['inclusos']

            try:
                data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d')
            except ValueError:
                flash('Data inválida.')
                return redirect(url_for('viagem_controller.cadastrar_viagem'))

            try:
                data_fim = datetime.strptime(data_fim, '%Y-%m-%d')
            except ValueError:
                flash('Data inválida.')
                return redirect(url_for('viagem_controller.cadastrar_viagem'))

            viagemRepository.createViagem(destino, data_inicio, data_fim, preco, qtd_assentos, assentos_indisponiveis, imagem_url, descricao, inclusos)
            flash('Viagem adicionada com sucesso.')
            return redirect(url_for('viagem_controller.index'))
        return render_template('cadastrar_viagem.html', url='/cadastrar_viagem')
    print('somente administradores podem ter acesso a esta página')
    return redirect(url_for('viagem_controller.index'))

@admin_controller.route('/delete_viagem/<int:viagem_id>', methods=['GET'])
def delete_viagem(viagem_id):
    viagemRepository.deleteViagem(viagem_id)
    return redirect(url_for('admin_controller.index'))

@admin_controller.route('/update_viagem/<int:viagem_id>', methods=['GET', 'POST'])
def update_viagem(viagem_id):
    viagem = viagemRepository.getViagem(viagem_id)
    if request.method == 'POST':
        destino = request.form['destino']
        data_inicio = request.form['data_inicio']
        data_fim = request.form['data_fim']
        preco = request.form['preco']
        qtd_assentos = request.form['qtd_assentos']
        viagem_url = request.form['viagem_url']
        try:
            preco = float(preco)
            data = datetime.strptime(data, '%Y-%m-%d')
        except ValueError:
            flash('Preço deve ser um número e data deve estar no formato YYYY-MM-DD.')
            return redirect(url_for('admin_controller.cadastrar_viagem'))
        viagemRepository.updateViagem(viagem, destino, data_inicio, data_fim, preco, qtd_assentos, assentos_indisponiveis=None) #viagem_url)
        flash('Viagem atualizada com sucesso.')
        return redirect(url_for('admin_controller.index'))
    return render_template('update_viagem.html', viagem=viagem)