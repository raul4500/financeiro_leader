from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask import session as cookies_session
from database import*
from repository.__init__ import*
from datetime import*

pagamento_controller = Blueprint('pagamento_controller', __name__)

pagamaentoRepository = PagamentoRepository()

@pagamento_controller.route('/registrar_pagamento/<int:id>', methods=['GET', 'POST'])
def novo_pagamento(id):
    if request.method == 'POST':
        valor = request.form['valor']
        data_pagamento = request.form['data_pagamento']
        data_pagamento = datetime.strptime(data_pagamento, '%Y-%m-%d').date()
        pagamaentoRepository.createPagamento(id , data_pagamento, valor, status='Confirmado')
        flash('Pagamento registrado com sucesso!', 'success')
        return redirect(url_for('controller.index'))
    return render_template('pagamento.html', url=id)