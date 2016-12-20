from setuptools import setup

setup(
    name='lektor-template-datetime',
    version='0.1',
    author=u'Felipe Martin',
    author_email='me@fmartingr.com',
    license='MIT',
    py_modules=['lektor_template_datetime'],
    entry_points={
        'lektor.plugins': [
            'template-datetime = lektor_template_datetime:TemplateDatetimePlugin',
        ]
    }
)
