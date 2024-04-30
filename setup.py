#!/usr/bin/env jython
# pylint: skip-file
"""incendium."""

from codecs import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

about = {}
with open(path.join(here, "src", "incendium", "__version__.py"), "r") as f:
    exec(f.read(), about)

with open("README.md", "r", "utf-8") as f:
    readme = f.read()

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    url=about["__url__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    license=about["__license__"],
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
        "ignition-api>=8.1.0;platform_python_implementation != 'Jython'",
        "typing;platform_python_implementation == 'Jython'",
    ],
    project_urls={
        "Documentation": "https://github.com/ignition-incendium/incendium/wiki",
        "Funding": "https://github.com/sponsors/cesarcoatl",
        "Source": "https://github.com/ignition-incendium/incendium",
        "Tracker": "https://github.com/ignition-incendium/incendium/issues",
    },
)
