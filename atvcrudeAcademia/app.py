from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

def ligar_banco():
    banco = psycopg2.connect(
        database="academia2B",
        host="localhost",
        port="5432",
        user="postgres",
        password="senai"
    )
    return banco


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/alunos")
def exibir_alunos():
    banco = ligar_banco()
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM aluno")
    lista = cursor.fetchall()
    banco.close()
    return render_template("alunos.html", lista=lista)


@app.route("/alunos/enviar", methods=["POST"])
def criar_aluno():
    nome = request.form["nome"]
    plano = request.form["plano"]
    idade = request.form["idade"]
    mensalidade = request.form["mensalidade"]

    banco = ligar_banco()
    cursor = banco.cursor()
    cursor.execute("""
        INSERT INTO aluno (nome, plano, idade, mensalidade)
        VALUES (%s, %s, %s, %s)
    """, (nome, plano, idade, mensalidade))
    banco.commit()
    banco.close()
    return redirect("/alunos")


@app.route("/alunos/editar/<int:id>")
def editar_aluno(id):
    banco = ligar_banco()
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM aluno WHERE id = %s", (id,))
    aluno = cursor.fetchone()
    banco.close()
    return render_template("editar_aluno.html", aluno=aluno)


@app.route("/alunos/atualizar/<int:id>", methods=["POST"])
def atualizar_aluno(id):
    nome = request.form["nome"]
    plano = request.form["plano"]
    idade = request.form["idade"]
    mensalidade = request.form["mensalidade"]

    banco = ligar_banco()
    cursor = banco.cursor()
    cursor.execute("""
        UPDATE aluno
        SET nome = %s, plano = %s, idade = %s, mensalidade = %s
        WHERE id = %s
    """, (nome, plano, idade, mensalidade, id))
    banco.commit()
    banco.close()
    return redirect("/alunos")


@app.route("/alunos/excluir/<int:id>", methods=["POST"])
def excluir_aluno(id):
    banco = ligar_banco()
    cursor = banco.cursor()
    cursor.execute("DELETE FROM aluno WHERE id = %s", (id,))
    banco.commit()
    banco.close()
    return redirect("/alunos")

#---------------------------------------Divisoria----------------------------------#
@app.route("/instrutores")
def exibir_instrutores():
    banco = ligar_banco()
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM instrutor")
    lista = cursor.fetchall()
    banco.close()
    return render_template("instrutores.html", lista=lista)


@app.route("/instrutores/enviar", methods=["POST"])
def criar_instrutor():
    nome = request.form["nome"]
    especialidade = request.form["especialidade"]
    carga_horaria = request.form["carga_horaria"]
    data_admissao = request.form["data_admissao"]

    banco = ligar_banco()
    cursor = banco.cursor()
    cursor.execute("""
        INSERT INTO instrutor (nome, especialidade, carga_horaria, data_admissao)
        VALUES (%s, %s, %s, %s)
    """, (nome, especialidade, carga_horaria, data_admissao))
    banco.commit()
    banco.close()
    return redirect("/instrutores")


@app.route("/instrutores/editar/<int:id>")
def editar_instrutor(id):
    banco = ligar_banco()
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM instrutor WHERE id = %s", (id,))
    instrutor = cursor.fetchone()
    banco.close()
    return render_template("editar_instrutor.html", instrutor=instrutor)


@app.route("/instrutores/atualizar/<int:id>", methods=["POST"])
def atualizar_instrutor(id):
    nome = request.form["nome"]
    especialidade = request.form["especialidade"]
    carga_horaria = request.form["carga_horaria"]
    data_admissao = request.form["data_admissao"]

    banco = ligar_banco()
    cursor = banco.cursor()
    cursor.execute("""
        UPDATE instrutor
        SET nome = %s, especialidade = %s, carga_horaria = %s, data_admissao = %s
        WHERE id = %s
    """, (nome, especialidade, carga_horaria, data_admissao, id))
    banco.commit()
    banco.close()
    return redirect("/instrutores")


@app.route("/instrutores/excluir/<int:id>", methods=["POST"])
def excluir_instrutor(id):
    banco = ligar_banco()
    cursor = banco.cursor()
    cursor.execute("DELETE FROM instrutor WHERE id = %s", (id,))
    banco.commit()
    banco.close()
    return redirect("/instrutores")

@app.route("/visualizar_alunos")
def visualizar_alunos():
    banco = ligar_banco()
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM aluno")
    lista = cursor.fetchall()
    banco.close()
    return render_template("visualizar_alunos.html", lista=lista)


@app.route("/visualizar_instrutores")
def visualizar_instrutores():
    banco = ligar_banco()
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM instrutor")
    lista = cursor.fetchall()
    banco.close()
    return render_template("visualizar_instrutores.html", lista=lista)



if __name__ == "__main__":
    app.run(debug=True)
