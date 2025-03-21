from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask import session as cookies_session
from database import*
from repository.__init__ import*
from datetime import*

viagem_controller = Blueprint('viagem_controller', __name__)

viagemRepository = ViagemRepository()
clienteRepository = PassageiroRepository()
passageiroRepository = PassageiroRepository()

@viagem_controller.route('/viagens')
def index():
    viagens = viagemRepository.getAllViagens()
    return render_template('viagens.html', viagens=viagens)

@viagem_controller.route('/cadastrar_viagem', methods=['GET','POST'])
def cadastrar_viagem():
    if request.method == 'POST':
        destino = request.form['destino']
        data_inicio = request.form['data_inicio']
        data_fim = request.form['data_fim']
        preco = request.form['preco']
        qtd_assentos = request.form['qtd_assentos']
        assentos_indisponiveis = None
        tipo_onibus = request.form.get('tipo_onibus')
        descricao = request.form['descricao']
        inclusos = request.form['inclusos']
        try:
            data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d')
        except ValueError:
            flash('Data inválida.', 'error')
            return redirect(url_for('viagem_controller.index'))
        try:
            data_fim = datetime.strptime(data_fim, '%Y-%m-%d')
        except ValueError:
            flash('Data inválida.', 'error')
            return redirect(url_for('viagem_controller.index'))
        viagemRepository.createViagem(destino, data_inicio, data_fim, preco, qtd_assentos, assentos_indisponiveis, tipo_onibus, descricao, inclusos)
        flash('Viagem adicionada com sucesso.', 'success')
        return redirect(url_for('viagem_controller.index'))
    return redirect(url_for('viagem_controller.index'))

@viagem_controller.route('/delete_viagem/<int:viagem_id>', methods=['GET'])
def delete_viagem(viagem_id):
    viagemRepository.deleteViagem(viagem_id)
    return redirect(url_for('viagem_controller.index'))

@viagem_controller.route('/update_viagem/<int:viagem_id>', methods=['GET', 'POST'])
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
            return redirect(url_for('viagem_controller.cadastrar_viagem'))
        viagemRepository.updateViagem(viagem, destino, data_inicio, data_fim, preco, qtd_assentos, assentos_indisponiveis=None) #viagem_url)
        flash('Viagem atualizada com sucesso.')
        return redirect(url_for('viagem_controller.index'))
    return render_template('update_viagem.html', viagem=viagem)

@viagem_controller.route('/viagem/<int:viagem_id>')
def teste(viagem_id):
    passageiros = passageiroRepository.getAllPassageiros()
    viagem = viagemRepository.getViagem(viagem_id)
    return render_template('tesste.html', passageiros=passageiros, viagem=viagem)


#    min_price = request.args.get('min_price', 0, type=int)
#    max_price = request.args.get('max_price', float('inf'), type=int)
#    month = request.args.get('month', None, type=int)
#    destination = request.args.get('destination', None, type=str)
#    viagens = get_viagens(min_price, max_price, month, destination)
#    usuario = cookies_session.get('usuario_email')
#    cliente = clienteRepository.getClienteByEmail(usuario)
#    #if usuario:
#    #    print(usuario)
#    itens = []
#    for viagem in viagens:
#        itens.append(viagem.destino)
#    return render_template('index.html', viagens=viagens, usuario=usuario, cliente=cliente, lista=itens)
#
#def get_viagens(min_price, max_price, month=None, destination=None):
#    if destination:
#        destination_words = destination.split()
#    if destination and month:
#        viagens = viagemRepository.getViagemByDestinationAndMonth(destination, month)
#        return [viagem for viagem in viagens if min_price <= viagem.preco <= max_price and any(word.lower() in viagem.destino.lower() for word in destination_words)]
#    if destination:
#        viagens = viagemRepository.getAllViagens()
#        return [viagem for viagem in viagens if min_price <= viagem.preco <= max_price and any(word.lower() in viagem.destino.lower() for word in destination_words)]
#    if month:
#        viagens = viagemRepository.getViagemByMonth(month)
#        return [viagem for viagem in viagens if min_price <= viagem.preco <= max_price]
#    else:
#        viagens = viagemRepository.getAllViagens()
#        return [viagem for viagem in viagens if min_price <= viagem.preco <= max_price]
#
#@viagem_controller.route('/add_assento/<int:viagem_id>', methods=['GET', 'POST'])
#def add_assento(viagem_id):
#    if request.method == 'POST':
#        assento = request.form['assento']
#        try:
#            assento = int(assento)
#        except ValueError:
#            flash('Assento deve ser um número.')
#            return redirect(url_for('viagem_controller.add_assento', viagem_id=viagem_id))
#
#        viagem = viagemRepository.getViagemById(viagem_id)
#        if viagem:
#            if viagem.assentos_disponiveis is None:
#                viagem.assentos_disponiveis = []
#            viagem.assentos_disponiveis.append(assento)
#            db.session.commit()
#            flash('Assento adicionado com sucesso.')
#        else:
#            flash('Viagem não encontrada.')
#        return redirect(url_for('viagem_controller.index'))
#    return render_template('add_assento.html', viagem_id=viagem_id)
#
#@viagem_controller.route('/add')
#def add():
#    viagemRepository.createViagem('sp', datetime.strptime('2000-05-10', '%Y-%m-%d'), datetime.strptime('2000-01-02', '%Y-%m-%d'), 450, 50, 50, 'https://www.google.com/imgres?q=cataratas%20do%20igua%C3%A7u&imgurl=https%3A%2F%2Fwww.destino.foz.br%2Fwp-content%2Fuploads%2F2022%2F01%2F002-%25E2%2580%2593-Cataratas-do-Iguacu-e1663260066395.jpg&imgrefurl=https%3A%2F%2Fwww.destino.foz.br%2Fatrativo%2Fcataratas-do-iguacu%2F&docid=YIV-_8cJY3u7CM&tbnid=Rop8bFLIsAfZKM&vet=12ahUKEwjRsbGt1a-LAxXzu5UCHTTcCXcQM3oECEEQAA..i&w=1200&h=675&hcb=2&ved=2ahUKEwjRsbGt1a-LAxXzu5UCHTTcCXcQM3oECEEQAA', 'cataratas do iguaçu', 'cataratas')
#    return redirect(url_for('viagem_controller.index'))
#