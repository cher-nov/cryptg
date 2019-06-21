#!/usr/bin/env python3

import sys
import os
import glob
import time
import stat
import shutil
import subprocess

sys.dont_write_bytecode = True  # prevent __pycache__ on importing './setup.py'
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))
from setup import PACKAGE_NAME, PACKAGE_VERSION, ENVVAR_VERSION_SUFFIX


def execute(*args, module=False):
    # there's no standard portable way to call Python3 explicitly
    # https://docs.python.org/3/using/windows.html
    shell_args = (sys.executable, *(("-m",) if module else ()), *args)
    subprocess.check_call(shell_args)

def purge(skip_errors):
    # shutil.rmtree fails on read-only files in Windows
    # https://bugs.python.org/issue19643
    def remove_readonly(func, path, *_):
        os.chmod(path, stat.S_IWRITE)
        func(path)

    package_wildcard = "{}-{}*/".format(PACKAGE_NAME, PACKAGE_VERSION)
    for folder in ("build", "dist", PACKAGE_NAME+".egg-info",
            *glob.glob(package_wildcard)):
        try:
            shutil.rmtree(folder,
                          onerror=remove_readonly,
                          ignore_errors=skip_errors)
        except FileNotFoundError:
            pass

def main(args):
    if "testpip" in args:
        execute(
            "pip", "install",
            "--pre", "--force-reinstall", "--no-cache-dir",
            "--index-url", "https://test.pypi.org/simple/",
            "--extra-index-url", "https://pypi.org/simple",
            "{}=={}.*".format(PACKAGE_NAME, PACKAGE_VERSION),
            module=True
        )
        return

    purge(False)

    if "testpypi" in args:
        # https://test.pypi.org/help/#file-name-reuse
        # https://www.python.org/dev/peps/pep-0440/#developmental-releases
        os.environ[ENVVAR_VERSION_SUFFIX] =  "dev{}".format(int(time.time()))
        os.environ["TWINE_REPOSITORY_URL"] = "https://test.pypi.org/legacy/"

    try:
        execute("setup.py", "sdist")
        #execute("setup.py", "bdist_wheel")
        execute("twine", "upload", "dist/*", module=True)
    finally:
        purge(True)


if __name__ == '__main__':
    main(sys.argv)
