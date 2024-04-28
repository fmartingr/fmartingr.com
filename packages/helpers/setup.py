from setuptools import setup

setup(
    name="lektor-helpers",
    version="0.1",
    author="Felipe Martin",
    author_email="me@fmartingr.com",
    license="MIT",
    py_modules=["lektor_helpers"],
    entry_points={
        "lektor.plugins": [
            "helpers = lektor_helpers:HelpersPlugin",
        ]
    },
)
