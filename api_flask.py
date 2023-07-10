from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route('/index')
def index():
    # Ler a planilha de dados em formato JSON
    # Substitua esta parte do código com a lógica para ler a planilha de dados
    data = {'hello': 'world'}

    # Retornar a planilha de dados em formato JSON
    return jsonify(data)

if __name__ == '__main__':
    app.run()
