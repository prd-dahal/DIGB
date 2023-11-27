from rest_framework.exceptions import ValidationError


def validate_image_length(value):
    max_length = 2 * 1024 * 1024
    if len(value) > max_length:
        raise ValidationError(f"Image length exceeds {max_length} characters.")
