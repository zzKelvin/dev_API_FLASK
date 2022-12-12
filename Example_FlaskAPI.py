from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/<int:id>')
def pessoa(id):
    soma = 1 + id
    return jsonify({'id':id, 'nome':'Rafael', 'Profissao':'Desenvolvedor'})

@app.route('/mais/<int:valor1>/<int:valor2>/')
def mais(valor1,valor2):
    return jsonify({'soma' :valor1 + valor2})

@app.route('/soma', methods=['POST', 'GET'])
def soma():
    dados = request.data
    print(dados)
    return 'soma'


if __name__ == '__main__':
    app.run(debug=True)