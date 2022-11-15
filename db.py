import mysql.connector

cnx = mysql.connector.connect(user='root', password='admin', host='localhost', database='datafodas')


def cadastrar_candidato(numero, nome, partido, cargo, regiao, naturalidade, genero):
    cursor = cnx.cursor()
    values = numero, nome, partido, cargo, regiao, naturalidade, genero
    qr = 'insert into cadastro_candidato (numero, nome, partido, cargo, regiao, naturalidade, genero) ' \
         'values(%s, %s, %s, %s, %s, %s, %s)'
    cursor.execute(qr, values)
    cnx.commit()


def selecionar_candidato():
    cursor = cnx.cursor()
    qr = 'SELECT cadastro_candidato.nome, cadastro_candidato.id, cadastro_candidato.numero,' \
         ' cadastro_candidato.partido' \
         ' FROM cadastro_candidato'
    cursor.execute(qr)
    consulta = cursor.fetchall()
    return consulta


def cadastrar_voto(id_candidato):
    cursor = cnx.cursor()
    values = id_candidato,
    qr = 'insert into voto (id_candidato) values(%s)'
    cursor.execute(qr, values)
    cnx.commit()


def contar_votos():
    cursor = cnx.cursor()
    qr = 'select count(id_candidato), nome, partido, numero from voto, cadastro_candidato where' \
         ' voto.id_candidato=cadastro_candidato.id group by id_candidato ORDER by count(id_candidato) DESC;'
    cursor.execute(qr)
    consulta = cursor.fetchall()
    return consulta


def realizar_login(nome, senha):
    cursor = cnx.cursor()
    qr = 'select nome_login, senha from administrador where nome_login like "{}" and senha like "{}" '.format(nome,
                                                                                                              senha)
    cursor.execute(qr)
    verificacao = cursor.fetchall()
    return verificacao
