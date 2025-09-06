Files generated to help formal verification:
- check_certificate.lean  (Lean 3 script using rationals)
- check_certificate.v     (Coq script using QArith; contains an admitted lemma as placeholder)
Source JSON used: /mnt/data/interval_certificate_M20_N1000000_summary_final.json

How to use:
1) Install Lean 3 (with mathlib) or Coq (8.13+).
2) Open check_certificate.lean in VSCode with Lean plugin, or run `lean --run check_certificate.lean` to evaluate the #eval lines and test `norm_num` proof.
   For Coq: run `coqc check_certificate.v` to compile; open file in coqtop to interact. The lemma uses 'Admitted' as a placeholder; replace with concrete QArith steps or use Qcertificates.

Notes:
- I cannot run Lean or Coq in this environment. These scripts encode exact rationals from the certificate JSON (if present) and are ready for you to run locally.
