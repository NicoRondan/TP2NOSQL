from flask import Flask, render_template, request, redirect, url_for
import redis 
from functions import inicializar

app = Flask(__name__)
#IP address del host
host = '172.17.0.2'

def connect_db():
    conexion = redis.StrictRedis(host= host, port=6379, db=0, charset="utf-8", decode_responses=True)
    if(conexion.ping()):
        print("conectado al servidor de redis")
    else:
        print("error...")
    return conexion

"""Conexion con redis"""
db = connect_db()

"""Reiniciar bbdd"""
#db.flushdb()

"""Carga de datos a la bbdd"""
inicializar(db)

"""Persistencia de datos"""
def guardar():
    db.save()



"""Settings"""
app.secret_key = 'clavesecreta'


@app.route('/')
def index():
    #Obtener solamente los capitulos
    data = db.keys('[1-8]*')
    #Ordenar la lista
    data.sort()
    return render_template('index.html', data = data, db = db)


@app.route('/confirmar-pago', methods=['POST', 'GET'])
def confirmarPago():
    if request.method == 'GET':
        #Obtener parametros de la URL
        capitulo = request.args.get('capitulo')
        precio = request.args.get('precio')
        #obtener titulo de la bbdd
        titulo = db.hget(capitulo, 'titulo')
        data = [capitulo, titulo, precio]
        return render_template('confirmar-pago.html', data = data)
    elif request.method == 'POST':
        #Obtener parametros de la URL
        capitulo = request.args.get('capitulo')
        #generar key
        key = 'estado' + ' ' + capitulo
        #Actualizar estado
        db.set(key, 'alquilado')
        #establecer tiempo 24hs a segundos
        db.expire(key, 86400)
        #Volver al index.html
        return redirect(url_for('index'))


@app.route('/reservar')
def reservarCapitulo():
    #Obtener el capitulo
    capitulo = request.args.get('capitulo')
    #generar key
    key = 'estado' + ' ' + capitulo
    #Cambiar estado
    db.set( key, 'reservado')
    #establecer tiempo 4min a segundos
    db.expire(key, 240)
    #Volver al index.html
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=False)
    exit(guardar())

