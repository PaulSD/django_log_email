from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.mail.backends.console import EmailBackend as ConsoleEmailBackend
from django.core.mail import get_connection

class EmailBackend(ConsoleEmailBackend):

    def __init__(self, *args, **kwargs):
        log_file = getattr(settings, 'EMAIL_LOG_FILE', None)
        if not isinstance(log_file, str):
            raise ImproperlyConfigured('EMAIL_LOG_FILE is invalid: %r' % log_file)
        stream = open(log_file, 'ab')
        super(EmailBackend, self).__init__(*args, **dict(kwargs, stream=stream))
        self.backend = None
        backend_name = getattr(settings, 'EMAIL_LOG_BACKEND', None)
        if backend_name is not None:
            self.backend = get_connection(backend_name, **kwargs)

    def open(self):
        super(EmailBackend, self).open()
        if self.backend is not None:
            self.backend.open()

    def close(self):
        super(EmailBackend, self).close()
        if self.backend is not None:
            self.backend.close()

    def send_messages(self, email_messages):
        super(EmailBackend, self).send_messages(email_messages)
        if self.backend is not None:
            return self.backend.send_messages(email_messages)
        return len(email_messages)
