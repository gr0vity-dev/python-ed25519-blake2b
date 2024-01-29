from __future__ import print_function
import sys
import os
import timeit
from distutils.core import setup, Extension, Command
from distutils.util import get_platform


LONG_DESCRIPTION = """\
A fork of python-ed25519 that uses BLAKE2b instead of SHA512 as a hash function
as used in the NANO cryptocurrency.
Original code written by @warner on GitHub:
github.com/warner/python-ed25519

Python bindings to the Ed25519 public-key signature system.

This offers a comfortable python interface to a C implementation of the
Ed25519 public-key signature system (http://ed25519.cr.yp.to/), using the
portable 'ref' code from the 'SUPERCOP' benchmarking suite.

This system provides high (128-bit) security, short (32-byte) keys, short
(64-byte) signatures, and fast (2-6ms) operation. Please see the README for
more details.
"""

sources = ["src/ed25519-glue/ed25519module.c"]
sources.extend(["src/ed25519-supercop-ref/"+s
                for s in os.listdir("src/ed25519-supercop-ref")
                if s.endswith(".c") and s != "test.c"])

m = Extension("py_ed25519_blake2b._ed25519",
              include_dirs=["src/ed25519-supercop-ref"], sources=sources)


setup(name="py-ed25519-blake2b",
      version="0.1.0",
      description="Ed25519 public-key signatures (BLAKE2b fork)",
      long_description=LONG_DESCRIPTION,
      author="Janne Pulkkinen",
      author_email="jannepulk@gmail.com",
      maintainer="gr0vity",
      license="MIT",
      url="https://github.com/gr0vity-dev/python-ed25519-blake2b",
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
          "Programming Language :: Python :: 3.10",
          "Programming Language :: Python :: 3.11",
          "Programming Language :: Python :: 3.12",
          "Topic :: Security :: Cryptography",
      ],
      ext_modules=[m],
      packages=["py_ed25519_blake2b"],
      package_dir={"py_ed25519_blake2b": "src/ed25519"}
      )
