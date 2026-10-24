# Mesa de Trámites v0.1 · NovaSoft
# Responsable: Grupo 13 · Backend NovaSoft
# Consume la API del Sistema de Personal de Comercial Andina (puerto 5001).
import os, json, sqlite3, urllib.request
from datetime import datetime, timedelta
from flask import Flask, jsonify, request, send_from_directory

CARPETA = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(CARPETA, 'tramites.db')
PERSONAL = os.environ.get('PERSONAL_API', 'http://localhost:5001')
app = Flask(__name__, static_folder='static')

TIPOS = {
    'VAC': {'nombre': 'Solicitud de vacaciones', 'area': 1, 'plazo_dias': 3},
    'CON': {'nombre': 'Constancia de trabajo', 'area': 1, 'plazo_dias': 2},
    'REE': {'nombre': 'Reembolso de gastos', 'area': 2, 'plazo_dias': 5},
    'COM': {'nombre': 'Compra menor', 'area': 3, 'plazo_dias': 5},
    'ACC': {'nombre': 'Acceso a un sistema', 'area': 4, 'plazo_dias': 2},
}


def conectar():
    c = sqlite3.connect(BASE)
    c.row_factory = sqlite3.Row
    return c


def preparar_base():
    with conectar() as c:
        c.executescript('''
        CREATE TABLE IF NOT EXISTS tramites (
          id INTEGER PRIMARY KEY AUTOINCREMENT, tipo TEXT, detalle TEXT,
          solicitante TEXT, responsable TEXT, estado TEXT, creado TEXT, vence TEXT);
        CREATE TABLE IF NOT EXISTS historial (
          tramite_id INTEGER, fecha TEXT, quien TEXT, estado TEXT, comentario TEXT);''')


def personal(ruta):
    with urllib.request.urlopen(PERSONAL + ruta) as r:
        return json.loads(r.read())


@app.errorhandler(Exception)
def error(e):
    return jsonify({'error': f'{type(e).__name__}: {e}'}), 500


@app.get('/')
def inicio():
    return send_from_directory(app.static_folder, 'index.html')


@app.post('/api/login')
def login():
    return jsonify(personal('/trabajadores/' + request.json['codigo']))


@app.get('/api/tipos')
def tipos():
    return jsonify(TIPOS)


@app.post('/api/tramites')
def crear():
    d = request.json
    tipo = TIPOS[d['tipo']]
    gestores = [t for t in personal('/trabajadores')
                if t['area_id'] == tipo['area'] and t['rol'] == 'gestor']
    responsable = gestores[-1]['codigo']
    ahora = datetime.now()
    with conectar() as c:
        cur = c.execute('INSERT INTO tramites (tipo, detalle, solicitante, responsable, estado, creado, vence) '
                        'VALUES (?,?,?,?,?,?,?)',
                        (d['tipo'], d['detalle'], d['solicitante'], responsable, 'REGISTRADO',
                         ahora.isoformat(timespec='minutes'),
                         (ahora + timedelta(days=tipo['plazo_dias'])).isoformat(timespec='minutes')))
        c.execute('INSERT INTO historial VALUES (?,?,?,?,?)',
                  (cur.lastrowid, ahora.isoformat(timespec='minutes'), d['solicitante'], 'REGISTRADO', ''))
    return jsonify({'id': cur.lastrowid, 'responsable': responsable})


@app.get('/api/tramites')
def listar():
    codigo = request.args['codigo']
    with conectar() as c:
        filas = c.execute('SELECT * FROM tramites WHERE solicitante = ? OR responsable = ? ORDER BY id DESC',
                          (codigo, codigo)).fetchall()
    return jsonify([dict(f) for f in filas])


@app.post('/api/tramites/<int:id>/estado')
def cambiar_estado(id):
    d = request.json
    with conectar() as c:
        c.execute('UPDATE tramites SET estado = ? WHERE id = ?', (d['estado'], id))
        c.execute('INSERT INTO historial VALUES (?,?,?,?,?)',
                  (id, datetime.now().isoformat(timespec='minutes'), d['codigo'], d['estado'], d.get('comentario', '')))
    return jsonify({'id': id, 'estado': d['estado']})


@app.get('/api/destacados')
def destacados():
    nombres = {t['codigo']: t['nombre'] for t in personal('/trabajadores')}
    with conectar() as c:
        filas = c.execute("SELECT responsable, COUNT(*) AS cerrados FROM tramites "
                          "WHERE estado IN ('ATENDIDO','RECHAZADO') GROUP BY responsable "
                          "ORDER BY cerrados DESC").fetchall()
    return jsonify([{'nombre': nombres.get(f['responsable'], f['responsable']), 'cerrados': f['cerrados']}
                    for f in filas])


if __name__ == '__main__':
    preparar_base()
    app.run(port=5000)
