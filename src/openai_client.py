from openai import OpenAI

from .ai_client import AIClient, ChatResponse


class OpenAIClient(AIClient):
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        if not api_key:
            raise ValueError("API key e obrigatoria.")
        self._client = OpenAI(api_key=api_key)
        self._model = model

    def send_prompt(self, prompt: str) -> ChatResponse:
        completion = self._client.chat.completions.create(
            model=self._model,
            messages=[{"role": "user", "content": prompt}],
        )
        choice = completion.choices[0]
        return ChatResponse(
            content=choice.message.content,
            model=completion.model,
            tokens_used=completion.usage.total_tokens,
        )
