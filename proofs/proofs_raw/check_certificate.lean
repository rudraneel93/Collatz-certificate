import tactic
-- Auto-generated Lean script to check numeric inequalities from certificate JSON.
-- Requires Lean 3 with core libraries. This file uses rational numbers (ℚ) and numeric normalization.
open_locale classical

def C_lower : ℚ := (10428213515294344342 : ℚ) / (1000000000000000000 : ℚ)
def C_upper : ℚ := (10428213515294344500 : ℚ) / (1000000000000000000 : ℚ)
def eps_cert : ℚ := (9250652510672808 : ℚ) / (10000000000000 : ℚ)
def N0 : ℕ := 1000000

example : (C_upper - C_lower) <= eps_cert :=
by norm_num

#eval C_lower
#eval C_upper
#eval eps_cert
