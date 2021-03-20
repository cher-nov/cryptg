use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

/// Encrypts the input plain text with the 32 bytes key and IV.
#[pyfunction]
fn encrypt_ige(plain: &[u8], key: &[u8], iv: &[u8]) -> Vec<u8> {
    todo!()
}

/// Decrypts the input cipher text with the 32 bytes key and IV.
#[pyfunction]
fn decrypt_ige(cipher: &[u8], key: &[u8], iv: &[u8]) -> Vec<u8> {
    todo!()
}

#[pymodule]
fn cryptg(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(encrypt_ige))?;
    m.add_wrapped(wrap_pyfunction!(decrypt_ige))?;
    Ok(())
}
