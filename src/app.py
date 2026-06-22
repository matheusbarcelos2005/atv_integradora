import os

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request

from .chat_service import ChatService
from .external_client import ExternalClient
from .message_validator import InvalidMessageError, MessageValidator


def create_app(service: ChatService = None) -> Flask:
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static",
    )

    if service is None:
        service = _build_default_service()

    @app.get("/")
    def index():
        return render_template("index.html")

    @app.post("/ask")
    def ask():
        payload = request.get_json(silent=True) or {}
        message = payload.get("message", "")
        try:
            response = service.ask(message)
            return jsonify({"content": response.content})
        except InvalidMessageError as error:
            return jsonify({"error": str(error)}), 400
        except Exception:
            return jsonify({"error": "Falha ao comunicar com o servico."}), 502

    return app


def _build_default_service() -> ChatService:
    load_dotenv()
    service_key = os.environ.get("SERVICE_KEY")
    if not service_key:
        raise RuntimeError(
            "Variavel SERVICE_KEY nao definida no ambiente."
        )
    endpoint = os.environ.get("SERVICE_URL")
    return ChatService(ExternalClient(service_key, endpoint), MessageValidator())


if __name__ == "__main__":
    create_app().run(host="127.0.0.1", port=5000, debug=True)
