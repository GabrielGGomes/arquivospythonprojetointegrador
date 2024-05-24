from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Contatos')
def contatos():
    return render_template('contatos.html')

@app.route('/Sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/Projeto')
def projeto():
    return render_template('projeto.html')

if __name__ == '__main__':
    app.run(debug=True)
