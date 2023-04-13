from setuptools import setup, find_packages

setup(
    name='project',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[        'Django==4.2',        'dj-database-url==1.3.0',        'django-heroku==0.3.1',        'gunicorn==20.1.0',        'Pillow==9.5.0',        'psycopg2-binary==2.9.6',        'sqlparse==0.4.3',        'typing_extensions==4.5.0',        'tzdata==2023.3',        'whitenoise==6.4.0'    ],

    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
