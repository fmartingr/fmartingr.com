from setuptools import setup


setup(
    name="lektor-sassify",
    version="0.1",
    py_modules=["lektor_sassify"],
    entry_points={
        "lektor.plugins": [
            "sassify = lektor_sassify:SassifyPlugin",
        ]
    },
    install_requires=["libsass==0.20.1"],
)
