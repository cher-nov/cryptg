#!/usr/bin/env python3

import cffi
from pycparser.ply import cpp, lex


# 'cffi' doesn't understand preprocessor directives properly, so we need this
def lazy_preprocess(source):
    pp = cpp.Preprocessor(lex.lex(module=cpp))
    pp.parse(source)
    result = ""
    while True:
        token = pp.token()
        if not token:
            return result
        result += token.value


ffibuilder = cffi.FFI()
with open("share/tiny-AES-c/aes.h", 'r') as f:
    header = f.read()
    ffibuilder.cdef(lazy_preprocess(header))
    ffibuilder.set_source(
        "_tinyaes_with_ige",
        header,
        sources=["share/tiny-AES-c/aes.c"]
    )

if __name__ == '__main__':
    ffibuilder.compile(verbose=True)
