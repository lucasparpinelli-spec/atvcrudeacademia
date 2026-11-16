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


if __name__ == '__main__':
    app.run()
