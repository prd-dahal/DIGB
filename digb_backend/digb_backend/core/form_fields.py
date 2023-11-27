from django.forms import CharField

from order_management.core import validators


class PhoneNumberField(CharField):
    default_validators = [validators.validate_phone_number]

    def __init__(self, **kwargs):
        super().__init__(strip=True, **kwargs)

