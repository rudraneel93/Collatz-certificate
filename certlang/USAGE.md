# CertLang Usage Guide

## Quick Start

### Running a CertLang Program

```bash
python3 interpreter/certlang_interpreter.py examples/basic_math.cl
```

### Running the Test Suite

```bash
python3 tests/test_certlang.py
```

### Running All Examples

```bash
./demo.sh
```

## CertLang File Extension

CertLang programs use the `.cl` file extension.

## Basic Syntax

### Variable Definition
```certlang
define variable_name: type = expression
```

### Verification
```certlang
verify boolean_expression
```

### Example Program
```certlang
define pi_approx: rational = 22/7
define epsilon: rational = 1/1000
verify abs(pi_approx - 314159/100000) <= epsilon
```

## Built-in Types

- `rational` - Exact rational numbers (e.g., `22/7`)
- `natural` - Non-negative integers (e.g., `42`)
- `integer` - All integers (e.g., `-17`)
- `interval` - Mathematical intervals (e.g., `interval(1/3, 2/3)`)

## Built-in Functions

- `abs(x)` - Absolute value
- `max(x, y)` - Maximum of two values
- `min(x, y)` - Minimum of two values
- `interval(lower, upper)` - Create an interval
- `width(interval)` - Width of an interval

## Examples Available

1. `examples/basic_math.cl` - Basic arithmetic and functions
2. `examples/numerical_analysis.cl` - Numerical analysis verification
3. `examples/collatz_cert.cl` - Collatz conjecture certificate verification

## Full Documentation

See `docs/certlang_book.md` for complete 8000-word documentation.