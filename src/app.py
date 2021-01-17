from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html')


@app.route('/form', methods=['POST', 'GET'])
def Form():
    
    return render_template('form.html')

@app.route('/confirmacion', methods=['POST','GET'])
def Confirm():
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    email = request.form.get('email')

    if not nombre or not apellido or not email:
        error = 'Todos los campos son requeridos'
        return render_template('error.html', error=error, nombre=nombre, apellido=apellido, email=email)
    
    return render_template('confirm.html',nombre= nombre, apellido= apellido)

if __name__=='__main__':
    app.run(debug=True) 