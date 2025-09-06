# Collatz Stopping-Time Certificate Repository

This repository packages the Collatz stopping-time research artifacts produced in this project. It is organized for easy upload to GitHub and one-click CI verification.

Contents:
- /paper: submission-ready paper in Word (.docx), PDF, and LaTeX sources (if available).
- /figures: all generated figures used in the paper.
- /code: scripts used to generate experiments, plots, Monte Carlo sampling, and data processing (if any).
- /proofs: Lean and Coq scripts to verify the numeric certificate and theorem template; exact rational data included.
- /data: JSON certificate files and sample outputs.

Notes:
- The Lean/Coq scripts include a numeric check that `(C_upper - C_lower) <= total_error` using exact rationals. To obtain a fully machine-checked proof, follow the README in /proofs that explains how to run Lean and Coq locally and how to formalize the final reduction lemmas.
