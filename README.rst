================
django_log_email
================

Django EMail backend that logs messages to a file before sending.

Usage
-----

Add the following to your ``requirements.txt``

::

  git+https://github.com/PaulSD/django_log_email

Then add the following to your ``local_settings.py``

::

  EMAIL_BACKEND = 'django_log_email.backends.EmailBackend'
  EMAIL_LOG_FILE = '/var/log/email.log'
  EMAIL_LOG_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

``EMAIL_LOG_BACKEND`` is optional.  If omitted, messages are logged but not actually sent.

License
-------

BSD
