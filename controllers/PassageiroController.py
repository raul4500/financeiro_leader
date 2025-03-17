from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask import session as cookies_session
from database import*
from repository.__init__ import*
from datetime import*
import re
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import *

passageiro_controller = Blueprint('passageiro_controller', __name__)

passageiroRepository = PassageiroRepository()

def verificarInfo(nome, email, nascimento, rg, telefone, senha):
    valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
    if nome == "" or email == "" or nascimento == "" or rg == "" or telefone == "" or senha == "":
        flash('Todos os campos são obrigatórios.')
        return False
    elif not valid:
        flash('Email inválido.')
        return False
    elif len(nome) < 3 or len(nome.strip().split(' ')) >= 2 or nome.endswith(' '):
        flash('Coloque seu nome completo.')
        return False
    elif len(rg) != 9:
        flash('RG deve ter 9 caracteres.')
        return False
    elif re.match(r'[a-wA-W]', rg):
        flash('Verique novamente o RG.')
        return False
    elif len(telefone) != 11:
        flash('Telefone deve ter 11 caracteres.')
        return False
    elif len(senha) < 8:
        flash('Senha deve ter no mínimo 8 caracteres.')
        return False
    elif telefone.isalpha():
        flash('Telefone deve conter apenas números.')
        return False
    elif not "@" in email:
        flash('Email inválido.')
        return False
    elif any(char.isdigit() for char in nome):
        flash('Nome não pode conter números.')
        return False
    return True

def validar_rg(rg):

    # Remove caracteres não numéricos
    rg = ''.join(filter(str.isdigit, rg))

    # Verifica se o RG possui 9 dígitos
    if len(rg) != 9:
        return False

    # Calcula o dígito verificador
    pesos = [2, 3, 4, 5, 6, 7, 8, 9]
    soma = 0
    for i in range(8):
        soma += int(rg[i]) * pesos[i]

    digito_verificador = soma % 11

    # Verifica se o dígito verificador calculado é igual ao dígito fornecido
    if digito_verificador == 10:
        digito_verificador = 'X'
    elif digito_verificador == 11:
        digito_verificador = 0

    return str(digito_verificador) == rg[8]

def editarInfo(nome, email, nascimento, telefone):
    valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
    if nome == "" or email == "" or nascimento == "" or telefone == "":
        flash('Todos os campos são obrigatórios.')
        return False
    elif not valid:
        flash('Email inválido.')
        return False
    elif len(nome) < 3 or len(nome.strip().split(' ')) >= 2 or nome.endswith(' '):
        flash('Coloque seu nome completo.')
        return False
    elif len(telefone) != 11:
        flash('Telefone deve ter 11 caracteres.')
        return False
    elif telefone.isalpha():
        flash('Telefone deve conter apenas números.')
        return False
    elif not "@" in email:
        flash('Email inválido.')
        return False
    elif any(char.isdigit() for char in nome):
        flash('Nome não pode conter números.')
        return False
    return True

@passageiro_controller.route('/add_passageiro', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        nascimento = request.form['nascimento']
        rg = request.form['rg']
        telefone = request.form['telefone']

        # Convert nascimento to a date object
        try:
            nascimento = datetime.strptime(nascimento, '%Y-%m-%d').date()
        except ValueError:
            flash('Data de Nascimento inválida.')
            return redirect(url_for('passageiro_controller.cadastrar'))

        # Check if RG already exists
        existing_passageiro = passageiroRepository.getPassageiroByRg(rg)
        if existing_passageiro:
            flash('RG já cadastrado.')
            return redirect(url_for('passageiro_controller.cadastrar'))
        
        # Check if email already exists
        existing_passageiro = passageiroRepository.getPassageiroByEmail(email)
        if existing_passageiro:
            flash('Email já cadastrado.')
            return redirect(url_for('passageiro_controller.cadastrar'))

        if verificarInfo(nome, email, nascimento, rg, telefone):
            passageiroRepository.createPassageiro(nome, email, nascimento, rg, telefone)
            return redirect(url_for('viagem_controller.index'))
        else:
            return redirect(url_for('passageiro_controller.cadastrar'))
    return render_template('cadastrar.html')

#@passageiro_controller.route('/login', methods=['GET', 'POST'])
#def login():
#    if request.method == 'POST':
#        email = request.form['email']
#        senha = request.form['senha']
#        c = passageiroRepository.getpassageiroByEmail(email)
#        if c:
#            if check_password_hash(c.senha, senha):
#                print('Login efetuado com sucesso')
#                cookies_session['usuario_senha'] = c.senha
#                cookies_session['usuario_email'] = email
#                return redirect(url_for('viagem_controller.index'))
#            else:
#                flash('Senha incorreta')
#                return redirect(url_for('passageiro_controller.login'))
#        else:
#            flash('Email não cadastrado')
#            return redirect(url_for('passageiro_controller.login'))
#    return render_template('login.html')

#@passageiro_controller.route('/perfil', methods=['GET','POST'])
#def perfil():
#    nome = request.args.get('nome', None, type=str)
#    rg = request.args.get('rg', None, type=str)
#    nascimento = request.args.get('nascimento', None, type=str)
#    novo_email = request.args.get('email', None, type=str)
#    telefone = request.args.get('telefone', None, type=str)
#    #print(nome)
#    #print(rg)
#    #print(nascimento)
#    #print(novo_email)
#    #print(telefone)
#    email = cookies_session['usuario_email']
#    if nome and rg and nascimento and novo_email and telefone:
#        c = passageiroRepository.getpassageiroByRg(rg)
#        if c:
#            if c.email != email:
#                print('Outra pessoa já possui esse RG')
#                return redirect(url_for('passageiro_controller.perfil'))
#        if email != novo_email:
#            if passageiroRepository.getpassageiroByEmail(novo_email):
#                print('Outra pessoa já possui esse Email')
#                return redirect(url_for('passageiro_controller.perfil'))
#        try:
#            nascimento = datetime.strptime(nascimento, '%Y-%m-%d').date()
#        except ValueError:
#            flash('Data de Nascimento inválida.')
#        if editarInfo(nome, novo_email, nascimento,telefone) and validar_rg(rg):
#            passageiroRepository.updatepassageiro(email, nome, novo_email, nascimento, rg, telefone)
#            email = novo_email
#        else:
#            flash('Há informações inválidas')   
#            return redirect(url_for('passageiro_controller.perfil'))
#    passageiro = passageiroRepository.getpassageiroByEmail(email)
#    return render_template('perfil.html', passageiro=passageiro, rg=list(passageiro.rg), len=len(list(passageiro.rg)))

#@passageiro_controller.route('/logout')
#def logout():
#    cookies_session.pop('usuario_email', None)
#    cookies_session.pop('usuario_senha', None)
#    return redirect(url_for('viagem_controller.index'))