from django.core.exceptions import ValidationError
import re
from django.utils.translation import gettext as _


class ConsecutivelyRepeatingCharacterValidator(object):
    def __init__(self, length=3):
        self.length = length

    def validate(self, password, user=None):
        for character in password:
            if password.count(character) >= self.length:
                check_character = character * self.length
                if check_character in password:
                    raise ValidationError(
                        _(
                            "The password contains characters that are consecutively repeating. e.g. 1111 or aaa"
                        ),
                    )

    def get_help_text(self):
        return _(
            "Characters in the password cannot consecutively repeat. e.g 111 or aaa"
        )


class ConsecutivelyIncreasingIntegerValidator(object):
    def __init__(self, length=3):
        self.length = length

    def validate(self, password, user=None):
        for character in password:
            if character.isdigit():
                count = 0
                number = int(character)
                index = password.index(character)

                try:
                    for i in range(1, self.length + 1):
                        if password[index + i].isdigit() and int(password[index + i]) == number + 1:
                            count += 1
                            number += 1

                            while count >= self.length:
                                raise ValidationError(
                                    _(
                                        "The password contains consecutively increasing integers. e.g 12345"
                                    ),
                                )
                except IndexError:
                    pass

    def get_help_text(self):
        return _(
            "Characters in the password cannot contain consecutively increasing integers. e.g 12345"
        )


class ConsecutivelyDecreasingIntegerValidator(object):
    def __init__(self, length=3):
        self.length = length

    def validate(self, password, user=None):
        for character in password:
            if character.isdigit():
                count = 0
                number = int(character)
                index = password.index(character)

                try:
                    for i in range(1, self.length + 1):
                        if password[index + i].isdigit() and int(password[index + i]) == number - 1:
                            count += 1
                            number -= 1

                            while count >= self.length:
                                raise ValidationError(
                                    _(
                                        "The password contains consecutively decreasing integers. e.g 54321"
                                    ),
                                )
                except IndexError:
                    pass

    def get_help_text(self):
        return _(
            "Characters in the password cannot contain consecutively decreasing integers. e.g 54321"
        )


class ContextValidator:
    def validate(self, password, user=None):
        context = [
            "context_word",
        ]

        for word in context:
            if word in password:
                raise ValidationError(
                    _("The password contains a variation of the company name"),
                )

    def get_help_text(self):
        return _("Password cannot be a variation of the company name.")


class UppercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                _("The password must contain at least 1 uppercase letter, A-Z."),
                code='password_no_upper',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 uppercase letter, A-Z."
        )


class LowercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[a-z]', password):
            raise ValidationError(
                _("The password must contain at least 1 lowercase letter, a-z."),
                code='password_no_lower',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 lowercase letter, a-z."
        )


class SymbolValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            raise ValidationError(
                _("The password must contain at least 1 symbol: " +
                  "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"),
                code='password_no_symbol',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 symbol: " +
            "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"
        )
