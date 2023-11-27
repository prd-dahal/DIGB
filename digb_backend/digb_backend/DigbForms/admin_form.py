from django import forms
from django.forms import formset_factory, BaseFormSet, inlineformset_factory

from digb_backend.DigbForms.models import RegistrationField, FormStep


class ChoiceAdminForm(forms.Form):
    choice = forms.CharField(
        max_length=55,
        required=False,
        initial=''
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['choice'].label = ''


class RegistrationFieldAdminForm(forms.ModelForm):
    has_choices = forms.BooleanField(initial=False, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.field_data and 'choices' in self.instance.field_data:
            self.initial['has_choices'] = True
        self.fields['field_type'].widget.attrs.update({
            'onchange': 'FieldTypeChange()'
        })

    def clean(self):
        has_choices = self.cleaned_data['has_choices']
        if not has_choices:
            # remove the choices key from the frontend validation
            # if key doesn't exist then it returns none
            if self.cleaned_data['field_data'].get('choices'):
                self.cleaned_data['field_data'].pop('choices', None)
        else:
            # getting formset total forms
            total_forms = int(self.data['form-TOTAL_FORMS'])
            # appending the formset form data to the json field only if the form has value
            choices = [
                self.data[f'form-{i}-choice'] for i in range(total_forms) if self.data[f'form-{i}-choice']
            ]
            self.cleaned_data['field_data'].update(
                {'choices': choices}
            )
        super().clean()

    class Meta:
        model = RegistrationField
        fields = (
            'form_step',
            'name',
            'order',
            'field_type',
            'frontend_field_type',
            'django_validation',
            'field_data',
            'has_choices',
        )


ChoiceAdminFormSet = formset_factory(
    ChoiceAdminForm,
    extra=0,
    can_delete=False,
    renderer=None,
)

RegistrationFieldAdminFormSet = inlineformset_factory(
    form=RegistrationFieldAdminForm,
    parent_model=FormStep,
    model=RegistrationField,
    extra=0,
    can_delete=False,
    renderer=None,
)
