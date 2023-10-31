// PYTHON -&&- RUST -==- MATURIN LIB
use pyo3::prelude::*;

fn fib(n: i32) -> i32 {
    if n <= 1 {
        return n;
    }
    fib(n - 1) + fib(n - 2)
}

#[pyfunction]
fn fib_to(nr: i32) {
    let mut i: i32 = 0;
    while i != nr {
        println!("{}", fib(i));
        i += 1;
    }
}

#[pyfunction]
fn sum(a: i32, b: i32) -> i32 {
    a + b
}

#[pyfunction]
fn sub(a: i32, b: i32) -> i32 {
    a - b
}

#[pyfunction]
fn mul(a: i32, b: i32) -> i32 {
    a * b
}

/// A Python module implemented in Rust.
#[pymodule]
fn lib_rs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(fib_to, m)?)?;
    m.add_function(wrap_pyfunction!(sum, m)?)?;
    m.add_function(wrap_pyfunction!(sub, m)?)?;
    m.add_function(wrap_pyfunction!(mul, m)?)?;
    Ok(())
}