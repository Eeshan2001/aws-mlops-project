from app.exception import ValidationException


class InputValidator:

    MIN_LENGTH = 15

    MAX_LENGTH = 5000

    @staticmethod
    def validate_text(text: str):

        if text is None:
            raise ValidationException(
                "Text cannot be None."
            )

        text = text.strip()

        if len(text) == 0:
            raise ValidationException(
                "Text cannot be empty."
            )

        if len(text) < InputValidator.MIN_LENGTH:
            raise ValidationException(
                f"Please enter at least {InputValidator.MIN_LENGTH} characters."
            )

        if len(text) > InputValidator.MAX_LENGTH:
            raise ValidationException(
                "Input text is too large."
            )

        return text