class PasswordValidationError(Exception):
    @staticmethod
    def when(condicao: bool, mensagem: str) -> None:
        if condicao:
            raise PasswordValidationError(mensagem)