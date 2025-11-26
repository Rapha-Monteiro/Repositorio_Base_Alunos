from flask import Flask, render_template, request, jsonify, redirect, url_for
from datetime import datetime
import json
import resend

# Adicionamos a chave de API para recebimento de email
resend.api_key = "re_UW8vNYs3_69ESVqHxzheFXpprC7V97qkK"

#Instanciamos a aplicação web
app= Flask(__name__)

# Comando para construir o banco de dados com as mensagens recebidas
with open('dados.json','r',encoding='utf-8') as arquivo:
    dados=json.load(arquivo)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        nome= request.form['name']
        email=request.form['email']
        mensagem=request.form['message']

# montar o dicionário da nova mensagem
        dados_mensagem={
            'nome':nome,
            'email':email,
            'mensagem':mensagem,
            'data':f'{datetime.today()}'
        }

# Adicionar e salvar no Json
        dados.append(dados_mensagem)
        with open('Dados.json','w',encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

# Envie e-mail usando Resend
            r = resend.Emails.send({
                "from": "onboarding@resend.dev",
                "to": "monteiroalunoprogramador@gmail.com",
                "subject": f"Solicitação de adoção{nome}",
                "html": f"<p>Email:{email}<br>{mensagem}</p>"
                })
# Após o POST - Redireciona para enviar reenvio do formulário
        return redirect(url_for('index')) # esse é um endpoint de retorno

# # GET - renderiza a página
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)