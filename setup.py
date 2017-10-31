import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "gmail",
    version = "0.0.5",
    author = "Tanay Agrawal",
    author_email = "FIXME",
    description = ("A Pythonic interface for Google Mail."),
    license = "MIT",
    keywords = "google gmail",
    url = "https://github.com/charlierguo/gmail",
    packages=['gmail'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Communications :: Email",
        "License :: OSI Approved :: MIT License",
    ],
)
