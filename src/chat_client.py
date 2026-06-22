from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class ChatResponse:
    content: str
    model: str
    tokens_used: int


class ChatClient(ABC):
    @abstractmethod
    def send_prompt(self, prompt: str) -> ChatResponse:
        raise NotImplementedError
