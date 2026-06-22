from .chat_client import ChatClient, ChatResponse
from .message_validator import MessageValidator


class ChatService:
    def __init__(self, client: ChatClient, validator: MessageValidator):
        self._client = client
        self._validator = validator

    def ask(self, message: str) -> ChatResponse:
        validated_message = self._validator.validate(message)
        return self._client.send_message(validated_message)
