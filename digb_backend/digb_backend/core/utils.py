import datetime
import os
import uuid
from io import BytesIO

import requests
from PIL import Image
from django.core.files import File
from django.core.files.storage import default_storage
from django.db.models import FileField
from django.utils.translation import gettext_lazy as _

from rest_framework.exceptions import ValidationError
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta


def generate_filename(filename, keyword):
    """
    Generates filename with uuid and a keyword
    :param filename: original filename
    :param keyword: keyword to be added after uuid
    :return: new filename in string
    """
    ext = filename.split('.')[-1]
    new_filename = "%s.%s" % (keyword, ext)
    return new_filename


def upload_to_folder(instance, filename, folder, keyword):
    """
    Generates the path where it should to uploaded

    :param instance: model instance
    :param filename: original filename
    :param folder: folder name where it should be stored
    :param keyword: keyword to be attached with uuid
    :return: string of new path
    """
    return os.path.join(folder, generate_filename(
        filename=filename,
        keyword=keyword
    ))


def update(instance, serializer_class, data):
    raise_errors_on_nested_writes('update', serializer_class, data)
    info = model_meta.get_field_info(instance)

    for attr, value in data.items():
        if attr in info.relations and info.relations[attr].to_many:
            field = getattr(instance, attr)
            field.set(value)
        else:
            setattr(instance, attr, value)
    instance.updated_at = datetime.datetime.now()
    instance.save()


def reduce_image_size(image, quality=70):
    image_extension = image.name.split('.')[-1]
    image_type = 'jpeg'
    if image_extension == 'png':
        image_type = 'png'
    try:
        img = Image.open(image)
    except FileNotFoundError:
        return image
    thumb_io = BytesIO()
    img.save(thumb_io, image_type, quality=quality)
    new_image = File(thumb_io, name=image.name)
    return new_image


def file_cleanup(sender, **kwargs):
    """
    File cleanup callback used to emulate the old delete
    behavior using signals. Initially django deleted linked
    files when an object containing a File/ImageField was deleted.
    """
    field_names = [f.name for f in sender._meta.get_fields()]
    for fieldname in field_names:
        try:
            field = sender._meta.get_field(fieldname)
        except:
            field = None

        if field and isinstance(field, FileField):
            inst = kwargs["instance"]
            f = getattr(inst, fieldname)
            m = inst.__class__._default_manager
            try:
                if (
                        hasattr(f, "path")
                        and os.path.exists(f.path)
                        and not m.filter(
                    **{"%s__exact" % fieldname: getattr(inst, fieldname)}
                ).exclude(pk=inst._get_pk_val())
                ):
                    default_storage.delete(f.path)
            except:
                pass


def validate_uuid(uuid_string):
    try:
        uuid.UUID(uuid_string)
    except ValueError:
        raise ValidationError({
            'non_field_errors': _('Not a valid UUID')
        })


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def is_email_disposable(email):
    response = requests.get(
        url=f'https://disposable.debounce.io/?email={email}'
    )
    print(response.json())
    if response.status_code == 200 and response.json().get('disposable') == 'true':
        return True
    return False
