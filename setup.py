from setuptools import setup

setup(
    name="assistant",
    version="1.0.0",
    author="Sam Larsen",
    author_email="sam@slarsen.io",
    license="MIT",
    python_requires=">=3.8",
    install_requires=[
        "openai ; python_version >= '3.8'",
        "python-dotenv ; python_version >= '3.8'"
    ]
)
