import os
from setuptools import find_packages, setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-telegram-login',
    version='0.2.3',
    packages = find_packages(
        exclude=[
            'login_app*',
            'django_telegram_tools',
        ]
    ),
    include_package_data=True,
    license='MIT',
    description='The reusable Django application for Telegram authorization (also known as Telegram login).',
    url='https://github.com/dmytrostriletskyi/django-telegram-login',
    author='Dmytro Striletskyi',
    author_email='dmytro.striletskyi@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
