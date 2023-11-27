from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import get_template


class BaseEmailMessage:
    template_name = None

    def __init__(self, context: dict, subject: str):
        self._subject = subject
        self._context = context

    def send(self, to: list, *args, **kwargs):
        mail = EmailMessage(
            subject=self._subject,
            body=self._get_message(),
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=to,
            reply_to=kwargs.pop('reply_to', []),
        )
        mail.content_subtype = "html"
        return mail.send()

    def _get_message(self):
        return get_template(self.template_name).render(self._context)