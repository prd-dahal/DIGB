from django.contrib import admin
from django_json_widget.widgets import JSONEditorWidget
from drf_core.admin import BaseModelAdmin
from django.db import models as db_models

from digb_backend.DigbForms import models
from digb_backend.DigbForms import admin_form


class RegistrationFieldAdminInline(admin.StackedInline):
    model = models.RegistrationField
    # formset = admin_form.RegistrationFieldAdminFormSet
    # form = admin_form.RegistrationFieldAdminForm
    extra = 0
    ordering = (
        'order',
    )


@admin.register(models.FormStep)
class FormStepAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'name',
    )

    list_filter = BaseModelAdmin.list_filter

    inlines = [
        RegistrationFieldAdminInline
    ]
    search_fields = ['name']

@admin.register(models.Registration)
class RegistrationAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'data',
    )

    list_filter = BaseModelAdmin.list_filter

    formfield_overrides = {
        # fields.JSONField: {'widget': JSONEditorWidget}, # if django < 3.1
        db_models.JSONField: {'widget': JSONEditorWidget},
    }


@admin.register(models.RegistrationField)
class RegistrationFieldAdmin(BaseModelAdmin):
    form = admin_form.RegistrationFieldAdminForm
    change_form_template = 'admin/registration_change_form.html'

    autocomplete_fields = [
        'form_step'
    ]

    list_display = BaseModelAdmin.list_display + (
        'order',
        'name',
        'slug',
    )

    list_filter = BaseModelAdmin.list_filter + (
        'field_type',
        'frontend_field_type'
    )
    ordering = ('order',)

    readonly_fields = (
        'slug',
    )

    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):

        extra_context = extra_context or {}
        extra_context['choices_formset'] = admin_form.ChoiceAdminFormSet
        template_response = super().changeform_view(
            request=request,
            object_id=object_id,
            extra_context=extra_context
        )

        # if the request method is GET and the page is not redirected.
        if request.method == "GET" and template_response.status_code != 302:
            # load the choice formset
            choices_formset = template_response.context_data['choices_formset']
            # get form initial data from template response
            __form_initial = template_response.context_data['adminform'].form.initial

            # check if there is frontend validation
            field_data = __form_initial.get('field_data', None)
            if field_data:
                # check if there is choices in the frontend validation
                choices = field_data.get('choices', None)
                if choices:
                    choices = __form_initial['field_data']['choices']
                    # passing initial values to the formsets.
                    choices_formset = choices_formset(initial=[{'choice': choice} for choice in choices])
            template_response.context_data['choices_formset'] = choices_formset
        return template_response
