from src.domain.models import Password
from src.domain.password_generator import PasswordGenerator


class PasswordService:
    def __init__(self):
        self.generator = PasswordGenerator()

    def generate_password(
        self,
        length: int,
        use_uppercase: bool,
        use_lowercase: bool,
        use_numbers: bool,
        use_symbols: bool,
    ) -> Password:
        return self.generator.generate(
            length, use_uppercase, use_lowercase, use_numbers, use_symbols
        )
