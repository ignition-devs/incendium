#!/usr/bin/env jython
# pylint: skip-file
"""incendium."""

from codecs import open
from os import path

from setuptools import find_packages, setup

HERE = path.abspath(path.dirname(__file__))

ABOUT = {}
with open(path.join(HERE, "src", "incendium", "__about__.py"), "r") as f:
    exec(f.read(), ABOUT)

LONG_DESCRIPTION = ""
with open("README.md", "r", "utf-8") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name=ABOUT["__title__"],
    version=ABOUT["__version__"],
    description=ABOUT["__description__"],
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=ABOUT["__url__"],
    author=ABOUT["__author__"],
    author_email=ABOUT["__author_email__"],
    license=ABOUT["__license__"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Manufacturing",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2 :: Only",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: Jython",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="coatl-dev, hmi, ignition, inductive automation, scada",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=2.7, <3",
    install_requires=[
        "ignition-api>=8.3.0;platform_python_implementation != 'Jython'",
        "typing;platform_python_implementation == 'Jython'",
    ],
    project_urls={
        "Documentation": "https://github.com/ignition-devs/incendium/wiki",
        "Funding": "https://github.com/sponsors/cesarcoatl",
        "Source": "https://github.com/ignition-devs/incendium",
        "Tracker": "https://github.com/ignition-devs/incendium/issues",
    },
)
