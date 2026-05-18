from .ai_client import AIClient, ChatResponse
from .prompt_validator import PromptValidator


class ChatService:
    def __init__(self, client: AIClient, validator: PromptValidator):
        self._client = client
        self._validator = validator

    def ask(self, prompt: str) -> ChatResponse:
        validated_prompt = self._validator.validate(prompt)
        return self._client.send_prompt(validated_prompt)
