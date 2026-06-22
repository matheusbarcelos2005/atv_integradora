class InvalidMessageError(ValueError):
    pass


class MessageValidator:
    MIN_LENGTH = 1
    MAX_LENGTH = 4000

    def validate(self, message) -> str:
        if message is None:
            raise InvalidMessageError("Mensagem nao pode ser nula.")
        if not isinstance(message, str):
            raise InvalidMessageError("Mensagem deve ser uma string.")

        cleaned = message.strip()
        if len(cleaned) < self.MIN_LENGTH:
            raise InvalidMessageError("Mensagem nao pode estar vazia.")
        if len(cleaned) > self.MAX_LENGTH:
            raise InvalidMessageError(
                f"Mensagem excede o limite de {self.MAX_LENGTH} caracteres."
            )
        return cleaned
