use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

/// Encrypts the input plain text with the 32 bytes key and IV.
#[pyfunction]
fn encrypt_ige(plain: &[u8], key: &[u8], iv: &[u8]) -> PyResult<Vec<u8>> {
    let mut key_array = [0; 32];
    if key.len() != key_array.len() {
        return Err(pyo3::exceptions::PyValueError::new_err("len(key) != 32"));
    }
    key_array.copy_from_slice(key);

    let mut iv_array = [0; 32];
    if iv.len() != iv_array.len() {
        return Err(pyo3::exceptions::PyValueError::new_err("len(iv) != 32"));
    }
    iv_array.copy_from_slice(iv);

    Ok(grammers_crypto::encrypt_ige(plain, &key_array, &iv_array))
}

/// Decrypts the input cipher text with the 32 bytes key and IV.
#[pyfunction]
fn decrypt_ige(cipher: &[u8], key: &[u8], iv: &[u8]) -> PyResult<Vec<u8>> {
    let mut key_array = [0; 32];
    if key.len() != key_array.len() {
        return Err(pyo3::exceptions::PyValueError::new_err("len(key) != 32"));
    }
    key_array.copy_from_slice(key);

    let mut iv_array = [0; 32];
    if iv.len() != iv_array.len() {
        return Err(pyo3::exceptions::PyValueError::new_err("len(iv) != 32"));
    }
    iv_array.copy_from_slice(iv);

    Ok(grammers_crypto::decrypt_ige(cipher, &key_array, &iv_array))
}

#[pymodule]
fn cryptg(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(encrypt_ige))?;
    m.add_wrapped(wrap_pyfunction!(decrypt_ige))?;
    Ok(())
}
