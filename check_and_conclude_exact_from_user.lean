import tactic
open_locale classical

-- Exact rationals from user-provided certificate
def C_lower : ℚ := (52141067576471723699354534458178559415185013027024167533779 : ℚ) / (5000000000000000000000000000000000000000000000000000000000 : ℚ)
def C_upper : ℚ := (104282135152943447398709068916357118830370026054048335324573 : ℚ) / (10000000000000000000000000000000000000000000000000000000000 : ℚ)
def C_center : ℚ := (52141067576471723699354534458178559415185013027024167598033 : ℚ) / (5000000000000000000000000000000000000000000000000000000000 : ℚ)
def C_half : ℚ := (51403 : ℚ) / (4000000000000000000000000000000000000000000000000000000000 : ℚ)
def union_bad : ℚ := (97 : ℚ) / (1048576 : ℚ)
def tail_mass : ℚ := (1 : ℚ) / (8589934592 : ℚ)
def total_error : ℚ := (370026100426912307739257812500000000000000000000051403 : ℚ) / (4000000000000000000000000000000000000000000000000000000000 : ℚ)
def E_low_a : ℚ := (300000127156575491227414244427394158213183589766028405755043 : ℚ) / (100000000000000000000000000000000000000000000000000000000000 : ℚ)
def E_high_a : ℚ := (300000127156575491227414244427394120457 : ℚ) / (100000000000000000000000000000000000000 : ℚ)
def E_low_b : ℚ := (287681228157235084767676821784943595901222280627836427268701 : ℚ) / (1000000000000000000000000000000000000000000000000000000000000 : ℚ)
def E_high_b : ℚ := (57536245631447016953535364356988719180244456125567285525463 : ℚ) / (200000000000000000000000000000000000000000000000000000000000 : ℚ)
def N0 : ℕ := 1000000

-- Numeric check: interval width ≤ total_error
example : (C_upper - C_lower) <= total_error :=
by norm_num

#eval C_lower
#eval C_upper
#eval total_error
#eval union_bad
#eval tail_mass
#eval C_half

-- Theorem template (requires formalizing reduction_correct and interval bounds):
variable (C_N : ℕ → ℚ) (C_mean : ℚ)
variable (reduction_correct : ∀ (N : ℕ), N ≥ N0 → abs (C_N N - C_mean) ≤ (union_bad + tail_mass + C_half))
variable (interval_bounds : C_lower ≤ C_mean ∧ C_mean ≤ C_upper)
variable (sum_error_ok : (union_bad + tail_mass + C_half) ≤ total_error)

theorem final_certificate :
  (C_lower ≤ C_mean ∧ C_mean ≤ C_upper) →
  ((union_bad + tail_mass + C_half) ≤ total_error) →
  ∀ (N : ℕ), N ≥ N0 → abs (C_N N - C_mean) ≤ total_error :=
begin
  intros h_int h_err N hN,
  have h := reduction_correct N hN,
  calc abs (C_N N - C_mean) ≤ (union_bad + tail_mass + C_half) : h
                        ... ≤ total_error : h_err,
end
