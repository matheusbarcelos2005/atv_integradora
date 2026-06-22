import os
from flask import Flask, jsonify, render_template, request
from dotenv import load_dotenv

from .external_client import enviar_mensagem_api
from .utils import validar_mensagem

load_dotenv()

def create_app() -> Flask:
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static",
    )

    @app.get("/")
    def index():
        return render_template("index.html")

    @app.post("/ask")
    def ask():
        payload = request.get_json(silent=True) or {}
        mensagem = payload.get("message", "")
        
        try:
            # Valida a mensagem recebida do frontend
            mensagem_validada = validar_mensagem(mensagem)
            
            # Obtém credenciais da API do ambiente
            api_key = os.environ.get("API_KEY")
            api_url = os.environ.get("API_URL")
            
            if not api_key or not api_url:
                return jsonify({"error": "Configurações da API não definidas no servidor."}), 500
                
            # Envia a mensagem para o serviço externo
            resposta = enviar_mensagem_api(mensagem_validada, api_key, api_url)
            return jsonify({"content": resposta})
            
        except ValueError as error:
            # Trata erros de validação
            return jsonify({"error": str(error)}), 400
        except Exception:
            # Trata erros de conexão/comunicação
            return jsonify({"error": "Falha ao se comunicar com o serviço de chat."}), 502

    return app

if __name__ == "__main__":
    create_app().run(host="127.0.0.1", port=5000, debug=True)
