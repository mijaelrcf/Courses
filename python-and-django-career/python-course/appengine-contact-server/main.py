from flask import Flask, render_template, request
#from contact import Contact

app = Flask(__name__)

@app.route(r'/', methods=['GET'])
def contact_book():
    return render_template('contact_book.html')

@app.route(r'/add', methods=['GET', 'POST'])
def add_contact():
    if request.form:
        print(request.form.get('name'))
        print(request.form.get('phone'))
        print(request.form.get('email'))

    return render_template('add_contact.html')

# 1era version
#@app.route('/') 
#def hello_world():
    #return 'Hola, mundo - Python!!!.'
    #return render_template('contact_book.html')

if __name__ == "__main__":
    app.run()

# Crear templates con Jinja2
# Hasta ahora hemos creado programas que devuelven strings en la consola, 
# en una aplicación web debemos devolver HTML, pero debe ser HTML dinámico 
# que se ajusta de acuerdo a la información que tenemos.