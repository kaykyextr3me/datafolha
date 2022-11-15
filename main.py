from flask import Flask, render_template, request, redirect
import func
import db

app = Flask(__name__)


@app.route('/')
def tela_votar():
    candidatos = db.selecionar_candidato()
    return render_template('votar.html', candidatos=candidatos)


@app.route('/', methods=['POST'])
def votar():
    voto = request.form['votar_candidato']
    db.cadastrar_voto(voto)
    return render_template('FIM.html')


# ----------------------------------------------------------------------------------------------------------------------------------------------------#

@app.route('/login')
def tela_login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def realizar_login():
    nome = request.form['nome_login']
    senha = request.form['senha_login']

    verificao = db.realizar_login(nome, senha)

    if len(verificao) != 0:
        if request.form['acao'] == 'relatorio':
            return redirect('/relatorio')
        if request.form['acao'] == 'cadastro':
            return redirect('/cadastro_candidato')
    elif len(verificao) == 0:
        return render_template('login.html', msg='Usuario ou senha incorretos! Tente novamente')


# ----------------------------------------------------------------------------------------------------------------------------------------------------#


@app.route('/cadastro_candidato')
def tela_cadastro_candidato():
    estados = func.pegar_estado()
    return render_template('cadastro_candidato.html', estados=estados)


@app.route('/cadastro_candidato', methods=["POST"])
def cadastro_candidato():
    numero = request.form['numero_candidato']
    nome = request.form['nome_candidato']
    partido = request.form['partido_candidato']
    cargo = request.form['cargo_candidato']
    regiao = request.form['regiao_candidato']
    naturalidade = request.form['naturalidade_candidato']
    genero = request.form['genero_candidato']

    db.cadastrar_candidato(numero, nome, partido, cargo, regiao, naturalidade, genero)
    return render_template('cadastro_candidato.html')


# ----------------------------------------------------------------------------------------------------------------------------------------------------#


@app.route('/relatorio')
def tela_relatorio():
    votos = db.contar_votos()
    return render_template('relatorio.html', votos=votos)


app.run(debug=True)
