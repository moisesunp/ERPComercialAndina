# Sistema de Personal de Comercial Andina (simulado)
# Responsable: Grupo 4 · Desarrollo interno
# API de solo lectura para sistemas de terceros.
import os, sqlite3
from flask import Flask, jsonify

CARPETA = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(CARPETA, 'personal.db')
app = Flask(__name__)


def conectar():
    c = sqlite3.connect(BASE)
    c.row_factory = sqlite3.Row
    return c


def preparar_base():
    if not os.path.exists(BASE):
        with conectar() as c, open(os.path.join(CARPETA, 'datos.sql'), encoding='utf-8') as f:
            c.executescript(f.read())


@app.get('/areas')
def areas():
    with conectar() as c:
        return jsonify([dict(r) for r in c.execute('SELECT * FROM areas')])


@app.get('/trabajadores')
def trabajadores():
    with conectar() as c:
        return jsonify([dict(r) for r in c.execute('SELECT * FROM trabajadores')])


@app.get('/trabajadores/<codigo>')
def trabajador(codigo):
    with conectar() as c:
        r = c.execute('SELECT * FROM trabajadores WHERE codigo = ?', (codigo,)).fetchone()
    if r is None:
        return jsonify({'codigo': 'NO_ENCONTRADO', 'mensaje_usuario': 'El trabajador no existe.'}), 404
    return jsonify(dict(r))


if __name__ == '__main__':
    preparar_base()
    app.run(port=5001)
