from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
from drf_core.models import BaseModel
from django.utils.translation import gettext_lazy as _


from digb_backend.DigbForms import utils


class FormStep(BaseModel):
    """
    This model represents the section of registration
    """
    name = models.CharField(
        max_length=60,
        help_text=_('Represents Section in mobile app')
    )
    order = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.name


class RegistrationField(BaseModel):
    """
    This model represents the registration fields for a particular event
    """

    FIELD_TYPE_CHOICES = (
        ('CharField', 'CharField'),
        ('DateField', 'DateField'),
        ('TimeField', 'TimeField'),
        ('DateTimeField', 'DateTimeField'),
        ('IntegerField', 'IntegerField'),
        ('BooleanField', 'BooleanField'),
        ('FileField', 'FileField'),
    )

    FRONTEND_FIELD_TYPE_CHOICES = (
        ('text', 'Text'),
        ('select', 'Select'),
        ('multiple_select', 'MultipleSelect'),
        ('file', 'File'),
        ('check_box', 'CheckBox'),
        ('radio', 'Radio'),
    )

    form_step = models.ForeignKey(
        FormStep,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    name = models.CharField(max_length=255)
    slug = models.CharField(
        blank=True,
        default=''
    )
    order = models.PositiveSmallIntegerField(default=1)
    field_type = models.CharField(
        max_length=13,
        choices=FIELD_TYPE_CHOICES,
        db_index=True
    )

    frontend_field_type = models.CharField(
        max_length=15,
        choices=FRONTEND_FIELD_TYPE_CHOICES,
        default='text',
        db_index=True
    )

    django_validation = models.JSONField(
        blank=True,
        default=dict
    )

    field_data = models.JSONField(
        blank=True,
        default=dict
    )

    def clean(self, *args, **kwargs):
        if self._state.adding:
            if self.frontend_field_type == 'file' and self.field_type != 'FileField':
                raise ValidationError({
                    'field_type': _('Field Should Be FileField')
                })
            try:
                RegistrationField.objects.get(
                    order=self.order,
                    form_step=self.form_step,
                    is_archived=False
                )
                raise ValidationError({
                    'order': _('Field with same order already exists')
                })
            except RegistrationField.DoesNotExist:
                super().clean()

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.slug = slugify(self.name).replace('-', '_')

            # if filed django input field type is char-field
            if self.field_type == "CharField":
                self.django_validation.update(
                    utils.default_django_char_field_validation()
                )
            # for front-end field type
            if self.frontend_field_type == 'file':
                self.field_data.update(
                    {'format_type': 'file', 'required': 'true'}
                )
            if self.frontend_field_type == 'text':
                self.field_data.update(
                    utils.default_frontend_char_field_validation()
                )
            # elif self.frontend_field_type in ('check_box', 'multiple_select'):
            else:
                self.field_data.update(
                    utils.default_frontend_choices_field_validation()
                )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']


class Registration(BaseModel):
    """
    This model represents the registration field with its value
    """


    data = models.JSONField(
        default=dict
    )

