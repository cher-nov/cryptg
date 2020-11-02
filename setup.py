#!/usr/bin/env python3

import sys
import os

from setuptools import find_packages, setup

PACKAGE_NAME = "cryptg"
PACKAGE_VERSION = "0.2.post2"
ENVVAR_VERSION_SUFFIX = "PYPI_SETUP_VERSION_SUFFIX"

_PACKAGE_DEPENDENCIES = [
    "cffi>=1.0.0",  # TODO: they promise to separate _cffi_backend later
    "pycparser"  # CPython's 'cffi' contains that, bun not the PyPi's one
]


def main(args):
    with open("README.rst", encoding='utf-8') as f:
        long_description = f.read()

    url = "https://github.com/cher-nov/" + PACKAGE_NAME

    setup(
        name=PACKAGE_NAME,
        version=PACKAGE_VERSION+os.environ.get(ENVVAR_VERSION_SUFFIX, ""),
        description="Cryptographic utilities for Telegram.",
        long_description=long_description,
        long_description_content_type="text/x-rst",

        url=url,
        download_url=url+"/releases",

        author="Dmitry D. Chernov",
        author_email="blackdoomer@yandex.ru",

        license="CC0",

        # https://pypi.python.org/pypi?:action=list_classifiers
        classifiers=[
            "Development Status :: 4 - Beta",

            "Intended Audience :: Developers",
            "Topic :: Security :: Cryptography",

            "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",

            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6"
        ],
        keywords="telegram crypto cryptography mtproto aes",

        packages=find_packages(),
        python_requires=">=3.3",
        install_requires=_PACKAGE_DEPENDENCIES,
        setup_requires=_PACKAGE_DEPENDENCIES,
        cffi_modules=["build_ffi.py:ffibuilder"]
    )


if __name__ == '__main__':
    main(sys.argv)
