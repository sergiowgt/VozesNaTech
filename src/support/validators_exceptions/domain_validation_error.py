class DomainValidationError(Exception):
    @staticmethod
    def when(condicao: bool, mensagem: str) -> None:
        if condicao:
            raise DomainValidationError(mensagem)