from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/verificar_notas", methods=['POST'])
def verificar_notas():
    nome = request.form['nome']
    nota_1 = float (request.form['nota_1'])
    nota_2 = float (request.form['nota_2'])
    nota_3 = float (request.form['nota_3'])
    media = (nota_1 + nota_2 + nota_3) / 3
   


    caminho_arquivo = 'models/nota.txt'
    with open(caminho_arquivo, 'a') as arquivo:
        arquivo.write(f"{nome};{nota_1};{nota_2};{nota_3};{round(media, 2)};\n")

    return redirect("/")

@app.route("/verificar_nota")
def verificar_nota():
    notas = []
    caminho_arquivo = 'models/nota.txt'
    

    with open(caminho_arquivo, 'r') as arquivo:
        for nota in arquivo:
            item = nota.strip().split(';')
            notas.append({
                'nome': item [0],
                'nota_1': item [1],
                'nota_2': item [2],
                'nota_3': item [3],
                'media': item[4],
            })

    return render_template("verificar_nota.html", prod=notas)

app.run(host='127.0.0.1', port=80, debug=True)