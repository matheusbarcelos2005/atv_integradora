import pytest

from src.ai_client import AIClient, ChatResponse
from src.chat_service import ChatService
from src.prompt_validator import InvalidPromptError, PromptValidator


class RecordingAIClient(AIClient):
    def __init__(self):
        self.received_prompts = []

    def send_prompt(self, prompt: str) -> ChatResponse:
        self.received_prompts.append(prompt)
        return ChatResponse(content="ok", model="test-model", tokens_used=1)


@pytest.fixture
def recording_client():
    return RecordingAIClient()


@pytest.fixture
def service(recording_client):
    return ChatService(recording_client, PromptValidator())


class TestPromptValidation:
    def test_valid_prompt_is_returned_trimmed(self):
        validator = PromptValidator()
        assert validator.validate("  ola mundo  ") == "ola mundo"

    def test_empty_prompt_is_rejected(self):
        with pytest.raises(InvalidPromptError):
            PromptValidator().validate("")

    def test_whitespace_only_prompt_is_rejected(self):
        with pytest.raises(InvalidPromptError):
            PromptValidator().validate("   \n\t  ")

    def test_oversized_prompt_is_rejected(self):
        oversized = "a" * (PromptValidator.MAX_LENGTH + 1)
        with pytest.raises(InvalidPromptError):
            PromptValidator().validate(oversized)

    def test_none_prompt_is_rejected(self):
        with pytest.raises(InvalidPromptError):
            PromptValidator().validate(None)


class TestSendingPrompt:
    def test_service_forwards_prompt_to_client(self, service, recording_client):
        service.ask("Explique SOLID")
        assert recording_client.received_prompts == ["Explique SOLID"]

    def test_service_trims_prompt_before_sending(self, service, recording_client):
        service.ask("   com espacos extras   ")
        assert recording_client.received_prompts == ["com espacos extras"]

    def test_invalid_prompt_blocks_call_to_client(self, service, recording_client):
        with pytest.raises(InvalidPromptError):
            service.ask("")
        assert recording_client.received_prompts == []

    def test_service_supports_multiple_sequential_sends(self, service, recording_client):
        service.ask("primeiro")
        service.ask("segundo")
        service.ask("terceiro")
        assert recording_client.received_prompts == ["primeiro", "segundo", "terceiro"]
