from django.utils.text import slugify
# from drf_core.utils import generate_filename
import uuid


def generate_filename(filename):
    # Get the file extension from the original filename
    extension = filename.split('.')[-1]

    # Generate a unique filename using UUID
    unique_filename = f"{uuid.uuid4().hex}.{extension}"

    return unique_filename
def default_django_char_field_validation():
    return {
        "max_length": 255,
        "min_length": 2,
        "allow_blank": False,
        "allow_null": False,
        "required": False,
        "trim_whitespace": True
    }


def default_frontend_char_field_validation():
    return {
        "max_length": 255,
        "min_length": 2,
        "required": False,
        "trim_whitespace": True
    }


def default_frontend_choices_field_validation():
    return {
        "required": False,
    }


def default__field_validation():
    return {
        "max_length": 255,
        "allow_blank": False,
        "allow_null": False,
        "required": True,
        "trim_whitespace": True
    }


def default_field_validation():
    return {
        "required": False
    }


def default_form_data():
    return {
        "input_type": "text",
        "default": "",
        "label": "",
        "placeholder": "",
        "hide": False,
        "options": ""
    }


def upload_registration_file(instance, filename):
    """
      Returns path to upload to
      :param instance: instance of model
      :param filename: original filename
      :return: path
      """
    return 'registration/{}/{}'.format(
        slugify(instance.id),
        generate_filename(
            filename=filename,
            keyword=''
        )
    )
