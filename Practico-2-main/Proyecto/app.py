from string import hexdigits
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import hashlib


app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import db, Usuario, Ingrediente, Receta

@app.route('/')
def Inicio():
    return render_template("index.html")

@app.route('/Bienvenido', methods=['GET', 'POST'])
def ingreso():
    if request.method == 'POST':

        if not request.form['email'] or not request.form['password']: #Evalua si el usuario en si no ingreso nada
            return render_template('index.html')

        else:
            Usuario_actual= Usuario.query.filter_by(correo=request.form['email']).first() #Crea la variable Usuario_actual y le asigna el email ingresado en el form

            if Usuario_actual is None: #Comprueba si esta vacio
                return render_template('Error.html', error="Email no Registrado")

            else:
                password=(hashlib.md5(bytes(request.form['password'], encoding='utf-8'))).hexdigest() #Encripta la Password

                if (password==Usuario_actual.clave): #Compara el password ya hasheado con el de la base de datos
                    return render_template('Bienvenido.html', nombre=Usuario_actual.nombre) #Redirecciona al usuario al template de Bienvenido.html
                else:
                    return render_template('Error.html', error="Contraseña incorrecta")
    else:
        return render_template('Ingreso.html', error = 'User or Password wrong') #El caso base lo redirecciona al Ingreso.html


if __name__=="__main__":
    db.create_all()
    app.run(debug = True)
    