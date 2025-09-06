# Collatz certificate repository (auto-generated)

This repository contains the numeric certificate and proof-check artifacts for the Collatz stopping-time constant project.

## Contents
- `check_and_conclude_exact_from_user.lean`    : Lean 3 script with exact rationals and theorem template.
- `check_and_conclude_exact_from_user.v`       : Coq script with exact rationals and theorem template.
- `check_certificate.lean`, `check_certificate.v`: simpler numeric check files.
- `.github/workflows/ci-lean-coq.yml`          : CI workflow to run Lean and Coq checks on push (requires Lean tooling installation in runner).

## How to verify locally
```bash
# Lean
lean --run check_and_conclude_exact_from_user.lean

# Coq
coqc check_and_conclude_exact_from_user.v
```

## Notes
- The Lean file uses `norm_num` to check numeric rational inequalities.
- The heavy mathematical lemmas (finite-state reduction, interval arithmetic correctness) are left as hypotheses in the `final_certificate` theorem; they must be formalized separately for a fully closed proof.
