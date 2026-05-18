class InvalidPromptError(ValueError):
    pass


class PromptValidator:
    MIN_LENGTH = 1
    MAX_LENGTH = 4000

    def validate(self, prompt) -> str:
        if prompt is None:
            raise InvalidPromptError("Prompt nao pode ser nulo.")
        if not isinstance(prompt, str):
            raise InvalidPromptError("Prompt deve ser uma string.")

        cleaned = prompt.strip()
        if len(cleaned) < self.MIN_LENGTH:
            raise InvalidPromptError("Prompt nao pode estar vazio.")
        if len(cleaned) > self.MAX_LENGTH:
            raise InvalidPromptError(
                f"Prompt excede o limite de {self.MAX_LENGTH} caracteres."
            )
        return cleaned
