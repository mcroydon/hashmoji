try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from hashmoji import get_version

setup(
    name="hashmoji",
    version=get_version(),
    description="Visualize hashes and bytes with emoji.",
    author="Matt Croydon",
    author_email="mcroydon@gmail.com",
    long_description=open("README.rst", "r").read(),
    url="https://github.com/mcroydon/hashmoji",
    py_modules=["hashmoji"],
    scripts=["hashmoji.py"],
    test_suite="tests.test_suite",
    classifiers=[
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Operating System :: MacOS :: MacOS X",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3"
    ],
)