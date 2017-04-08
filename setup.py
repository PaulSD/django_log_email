from setuptools import setup
from django_log_email import __version__

setup(
    name = "django_log_email",
    version = __version__,
    description = ("Django EMail backend that logs messages to a file before sending"),
    url = "https://github.com/PaulSD/django_log_email",
    author = "Paul Donohue",
    license = "BSD",
    packages=['django_log_email'],
    install_requires=['Django >= 1.3'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe = False,
)
