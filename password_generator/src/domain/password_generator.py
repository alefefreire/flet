import random
import string

from src.domain.models import Password


class PasswordGenerator:
    def generate(
        self,
        length: int,
        use_uppercase: bool,
        use_lowercase: bool,
        use_numbers: bool,
        use_symbols: bool,
    ) -> Password:
        char_set = ""
        if use_uppercase:
            char_set += string.ascii_uppercase
        if use_lowercase:
            char_set += string.ascii_lowercase
        if use_numbers:
            char_set += string.digits
        if use_symbols:
            char_set += string.punctuation

        if not char_set:
            raise ValueError("At least one character set must be selected")

        password_value = "".join(random.choices(char_set, k=length))
        return Password(value=password_value)
