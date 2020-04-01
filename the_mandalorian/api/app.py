from flask import Flask, render_template, request, redirect, url_for, flash
from database import Database

app = Flask(__name__)

#IP address del host
host = '172.17.0.2'

"""Conexion con redis"""
db = Database(host)

db2 = Database(host)

"""Reiniciar bbdd"""
#db.reiniciar()

"""Carga de datos a la bbdd"""
if db.vacia:
    db.inicializar()


"""Session"""
app.secret_key = 'clavesecreta'


@app.route('/')
def index():
    #Obtener solamente los capitulos
    formato = '[1-8]*'
    data = db.keys(formato)
    return render_template('index.html', data = data, db = db)


@app.route('/confirmar-pago', methods=['POST', 'GET'])
def confirmarPago():
    if request.method == 'GET':
        #Obtener parametros de la URL
        capitulo = request.args.get('capitulo')
        precio = request.args.get('precio')
        #obtener titulo de la bbdd
        titulo = db.hget(capitulo, 'titulo')
        #Generar key
        key = 'estado ' + capitulo
        if not(db.existe(key)):
            return redirect(url_for('index'))
        elif db.get(key) == 'alquilado':
            return redirect(url_for('index'))
        else:
            data = [capitulo, titulo, precio]
            return render_template('confirmar-pago.html', data = data)    
    elif request.method == 'POST':
        #Obtener parametros de la URL
        capitulo = request.args.get('capitulo')
        #generar key
        key = 'estado ' + capitulo
        #Actualizar estado
        db.set(key, 'alquilado')
        #establecer tiempo 24hs a segundos
        db.expire(key, 86400)
        #Volver al index.html
        flash('Pago Confirmado!')
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
    flash('Capitulo Reservado Satisfactoriamente!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=False)
    exit(db.guardar())

