use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn fib(n: i32) -> i32 {
    if n <= 1 {
        return n;
    }
    fib(n - 1) + fib(n - 2)
}

/// A Python module implemented in Rust.
#[pymodule]
fn lib_rs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(fib, m)?)?;
    Ok(())
}