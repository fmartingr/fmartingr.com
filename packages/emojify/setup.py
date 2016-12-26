from setuptools import setup

setup(
    name='lektor-emojify',
    version='0.1',
    author=u'Felipe Martin',
    author_email='me@fmartingr.com',
    license='MIT',
    py_modules=['lektor_emojify'],
    install_requires=['emoji'],
    entry_points={
        'lektor.plugins': [
            'emojify = lektor_emojify:EmojifyPlugin',
        ]
    }
)
