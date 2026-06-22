from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class ChatResponse:
    content: str


class ChatClient(ABC):
    @abstractmethod
    def send_message(self, message: str) -> ChatResponse:
        raise NotImplementedError
