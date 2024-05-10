from flask import Flask, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# URL da API do chatflow
API_URL = "http://localhost:3000/api/v1/prediction/e5cea08d-d59b-4688-b9f0-ad78dce11a79"

# Função que envia uma solicitação POST para a API com um payload e retorna a resposta JSON
def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()

@app.route('/')
def index():
    # Define um payload com a pergunta que será enviada para a API
    payload = { "question": "Hey, how are you?",}

    # Chama a função query para enviar o payload para a API e obter a resposta
    response = query(payload)

    # Extrai a resposta do chatbot da resposta da API
    chatbot_response = response["text"]

    # Renderiza o template (aqui chamado 'index.html'), passando a resposta do chatbot para ser exibida na página
    return render_template('index.html', chatbot_response=chatbot_response)

if __name__ == '__main__':
    app.run(debug=True)