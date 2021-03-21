use pyo3::{prelude::*, types::PyBytes, wrap_pyfunction};

/// Encrypts the input plain text with the 32 bytes key and IV.
#[pyfunction]
#[text_signature = "(plain, key, iv)"]
fn encrypt_ige(plain: &[u8], key: &[u8], iv: &[u8]) -> PyResult<Py<PyBytes>> {
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

    let cipher = grammers_crypto::encrypt_ige(plain, &key_array, &iv_array);
    Python::with_gil(|py| Ok(PyBytes::new(py, &cipher).into()))
}

/// Decrypts the input cipher text with the 32 bytes key and IV.
#[pyfunction]
#[text_signature = "(cipher, key, iv)"]
fn decrypt_ige(cipher: &[u8], key: &[u8], iv: &[u8]) -> PyResult<Py<PyBytes>> {
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

    let plain = grammers_crypto::decrypt_ige(cipher, &key_array, &iv_array);
    Python::with_gil(|py| Ok(PyBytes::new(py, &plain).into()))
}

#[pymodule]
fn cryptg(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(encrypt_ige))?;
    m.add_wrapped(wrap_pyfunction!(decrypt_ige))?;
    Ok(())
}
