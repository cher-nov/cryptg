#!/usr/bin/env python3

import _tinyaes_with_ige

_CTX_TYPEDEF = "struct AES_ctx*"


def encrypt_ige(plain, key, iv):
    """Encrypts the input plain text with the 32 bytes key and IV."""
    ctx = _tinyaes_with_ige.ffi.new(_CTX_TYPEDEF)
    _tinyaes_with_ige.lib.AES_init_ctx_iv32(ctx, key, iv)
    _tinyaes_with_ige.lib.AES_IGE_encrypt_buffer(ctx, plain, len(plain))
    return plain

def decrypt_ige(cipher, key, iv):
    """Decrypts the input cipher text with the 32 bytes key and IV."""
    ctx = _tinyaes_with_ige.ffi.new(_CTX_TYPEDEF)
    _tinyaes_with_ige.lib.AES_init_ctx_iv32(ctx, key, iv)
    _tinyaes_with_ige.lib.AES_IGE_decrypt_buffer(ctx, cipher, len(cipher))
    return cipher
