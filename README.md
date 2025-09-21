# Collatz Stopping-Time Certificate Repository

This repository packages the Collatz stopping-time research artifacts produced in this project. It is organized for easy upload to GitHub and one-click CI verification.

Contents:
- /paper: submission-ready paper in Word (.docx), PDF, and LaTeX sources (if available).
- /figures: all generated figures used in the paper.
- /code: scripts used to generate experiments, plots, Monte Carlo sampling, and data processing (if any).
- /proofs: Lean and Coq scripts to verify the numeric certificate and theorem template; exact rational data included.
- /data: JSON certificate files and sample outputs.
- **/certlang: CertLang - A new domain-specific language for mathematical certificate verification with complete implementation and 8000-word documentation.**

## CertLang - Mathematical Certificate Verification Language

CertLang is a specialized domain-specific language designed for expressing and verifying mathematical certificates. It features:

- **Exact rational arithmetic** - No floating-point errors
- **Declarative syntax** - Natural mathematical notation
- **Verification-focused design** - Built for certificate validation
- **Complete implementation** - Full interpreter in Python
- **Comprehensive documentation** - 8000-word guide and tutorial

### Quick Start

```bash
cd certlang
python3 interpreter/certlang_interpreter.py examples/collatz_cert.cl
```

See `certlang/README.md` and `certlang/docs/certlang_book.md` for complete documentation.

Notes:
- The Lean/Coq scripts include a numeric check that `(C_upper - C_lower) <= total_error` using exact rationals. To obtain a fully machine-checked proof, follow the README in /proofs that explains how to run Lean and Coq locally and how to formalize the final reduction lemmas.
- The same verification is now available in CertLang with a more accessible syntax in `certlang/examples/collatz_cert.cl`.
