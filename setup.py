# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='doorman',
    description='an osquery fleet manager',
    url='https://github.com/mwielgoszewski/doorman',
    version='0.3',
    packages=find_packages(
        exclude=[
            'tests*',
        ]
    ),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'alembic==0.8.6',
        'amqp==1.4.9',
        'anyjson==0.3.3',
        'bcrypt==2.0.0',
        'billiard==3.3.0.23',
        'blinker==1.4',
        'celery==3.1.23',
        'cffi==1.6.0',
        'contextlib2==0.5.3',
        'cssmin==0.2.0',
        'enum34==1.1.6',
        'Flask==0.10.1',
        'Flask-Assets==0.11',
        'Flask-Bcrypt==0.7.1',
        'Flask-DebugToolbar==0.10.0',
        'flask-ldap3-login==0.9.9',
        'Flask-Login==0.3.2',
        'Flask-Mail==0.9.1',
        'Flask-Migrate==1.8.0',
        'flask-paginate==0.4.1',
        'Flask-Script==2.0.5',
        'Flask-SQLAlchemy==2.1',
        'Flask-WTF==0.12',
        'itsdangerous==0.24',
        'Jinja2==2.8',
        'jsmin==2.2.1',
        'kombu==3.0.35',
        'ldap3==1.3.1',
        'Mako==1.0.4',
        'MarkupSafe==0.23',
        'oauthlib==1.1.1',
        'psycopg2==2.6.1',
        'pyasn1==0.1.9',
        'pycparser==2.14',
        'python-editor==1.0',
        'pytz==2016.4',
        'raven==5.20.0',
        'redis==2.10.5',
        'requests==2.10.0',
        'requests-oauthlib==0.6.1',
        'scales==1.0.9',
        'SQLAlchemy==1.0.12',
        'webassets==0.11.1',
        'Werkzeug==0.11.8',
        'WTForms==2.1',
    ],
    package_data={
        'resources': 'doorman/resources/*',
        'static': 'doorman/static/*',
        'templates': 'doorman/templates/*',
    }
)
