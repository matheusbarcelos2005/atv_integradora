import os

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request

from .chat_service import ChatService
from .openai_client import OpenAIClient
from .prompt_validator import InvalidPromptError, PromptValidator


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
        prompt = payload.get("prompt", "")
        try:
            response = service.ask(prompt)
            return jsonify(
                {
                    "content": response.content,
                    "model": response.model,
                    "tokens_used": response.tokens_used,
                }
            )
        except InvalidPromptError as error:
            return jsonify({"error": str(error)}), 400
        except Exception:
            return jsonify({"error": "Falha ao comunicar com a API."}), 502

    return app


def _build_default_service() -> ChatService:
    load_dotenv()
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Variavel OPENAI_API_KEY nao definida no ambiente."
        )
    model = os.environ.get("OPENAI_MODEL", "gpt-3.5-turbo")
    return ChatService(OpenAIClient(api_key, model), PromptValidator())


if __name__ == "__main__":
    create_app().run(host="127.0.0.1", port=5000, debug=True)
