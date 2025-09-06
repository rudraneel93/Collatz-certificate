# Collatz Stopping-Time Certificate Repository

[![CI](https://github.com/rudraneel93/Collatz-certificate/actions/workflows/ci-lean-coq.yml/badge.svg)](https://github.com/rudraneel93/Collatz-certificate/actions/workflows/ci-lean-coq.yml)

This repository packages the Collatz stopping-time research artifacts produced in this project. It is organized for easy upload to GitHub and one-click CI verification.

Contents:
- /paper: submission-ready paper in Word (.docx), PDF, and LaTeX sources (if available).
- /figures: all generated figures used in the paper.
- /code: scripts used to generate experiments, plots, Monte Carlo sampling, and data processing (if any).
- /proofs: Lean and Coq scripts to verify the numeric certificate and theorem template; exact rational data included.
- /data: JSON certificate files and sample outputs.

Quick start (local):
- Coq (Rocq 9.x):
  - coqc proofs/lean_coq/check_and_conclude_exact_from_user.v
- Lean 3 (optional):
  - lean -j1 proofs/lean_coq/check_and_conclude_exact_from_user.lean

Notes:
- The Lean/Coq scripts include a numeric check that `(C_upper - C_lower) <= total_error` using exact rationals. The CI verifies this automatically on push/PR.
