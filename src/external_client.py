import json
from urllib import request

from .chat_client import ChatClient, ChatResponse


class ExternalClient(ChatClient):
    def __init__(self, service_key: str, endpoint: str):
        if not service_key:
            raise ValueError("Chave do servico e obrigatoria.")
        if not endpoint:
            raise ValueError("URL do servico e obrigatoria.")
        self._service_key = service_key
        self._endpoint = endpoint

    def send_message(self, message: str) -> ChatResponse:
        payload = json.dumps({"message": message}).encode("utf-8")
        req = request.Request(
            self._endpoint,
            data=payload,
            headers={
                "Authorization": f"Bearer {self._service_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )

        with request.urlopen(req, timeout=30) as response:
            data = json.loads(response.read().decode("utf-8"))

        content = data.get("content") or data.get("response") or ""
        return ChatResponse(content=content)
