import uuid
from django.core.exceptions import ValidationError
from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from digb_backend.core import managers


class BaseModel(models.Model):
    """
    Base Model that will be used in this project
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    is_archived = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    objects = managers.BaseModelManager()

    def archive(self):
        if self.is_archived:
            raise DjangoValidationError({
                'non_field_errors': _('Failed - it is already archived.')
            })
        self.is_archived = True
        self.updated = timezone.now()
        self.save(update_fields=['is_archived', 'updated'])

    def restore(self):
        if not self.is_archived:
            raise DjangoValidationError({
                'non_field_errors': _('Failed - it is already restored.')
            })
        self.is_archived = False
        self.updated = timezone.now()
        self.save(update_fields=['is_archived', 'updated'])


class BasePublishModel(BaseModel):
    is_published = models.BooleanField(default=False)

    class Meta:
        abstract = True

    objects = managers.BasePublishModelManager()

    def publish(self):
        if self.is_published:
            raise DjangoValidationError({
                'non_field_errors': _('Failed - it is already published.')
            })
        self.is_published = True
        self.updated = timezone.now()
        self.save(update_fields=['is_published', 'updated'])

    def hide(self):
        if not self.is_published:
            raise DjangoValidationError({
                'non_field_errors': _('Failed - it is already hidden.')
            })
        self.is_published = False
        self.updated = timezone.now()
        self.save(update_fields=['is_published', 'updated'])




