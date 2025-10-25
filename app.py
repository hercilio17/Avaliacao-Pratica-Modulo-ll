from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# rota de soma 

@app.route("/soma")
def soma():
    valor1 = request.args.get("valor1", )
    valor2 = request.args.get("valor2", )

    resultado = valor1 + valor2

    return jsonify({"resultado": resultado})

# rota de subtração 

@app.route("/subtrair")
def subtrair():
    valor1 = request.args.get("valor1",)
    valor2 = request.args.get("valor2",)

    return jsonify({"resultado": resultado})

# rota de multiplicação 

@app.route("/multiplicaçao")
def multiplicar():
    valor1 = request.args.get("valor1", )
    valor2 = request.args.get("valor2", )

    return jsonify({"resultado": resultado})

# rota de divisão 

@app.route("/divisao")
def dividir():
    valor1 = request.args.get("valor1", )
    valor2 = request.args.get("valor2", )
    
    if valor2 == 0:

        return jsonify({"erro": "Divisao por zero não é permitida"}), 400

    resultado = valor1 / valor2
    return jsonify({"resultado": resultado})

if __name__ == '__main__':
    app.run(debug=True)