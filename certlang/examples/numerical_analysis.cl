# Numerical Analysis Certificate Verification
# This example shows how to verify numerical analysis results

# Define a function approximation and its error bounds
define f_exact: rational = 1000000/3  # Representing 1/3 * 10^6 
define f_approx: rational = 333333/1
define approx_error: rational = 1/3

# Verify the approximation error is within bounds
verify abs(f_exact - f_approx) <= approx_error

# Define integration bounds for a numerical integration certificate
define integral_lower: rational = 15707/10000  # π/2 ≈ 1.5707
define integral_upper: rational = 15709/10000
define integral_estimate: rational = 15708/10000

verify integral_lower <= integral_estimate
verify integral_estimate <= integral_upper

# Numerical series convergence verification
define series_partial_1: rational = 1/1
define series_partial_2: rational = 1/1 + 1/4
define series_partial_3: rational = 1/1 + 1/4 + 1/9
define series_limit_lower: rational = 164/100
define series_limit_upper: rational = 165/100

verify series_partial_1 <= series_partial_2
verify series_partial_2 <= series_partial_3
verify series_partial_3 <= series_limit_upper

# Root finding verification
define sqrt2_approx: rational = 1414/1000
define sqrt2_lower: rational = 141/100
define sqrt2_upper: rational = 142/100

verify sqrt2_lower <= sqrt2_approx
verify sqrt2_approx <= sqrt2_upper

# Verify the approximation satisfies the equation within tolerance
define sqrt2_squared: rational = sqrt2_approx * sqrt2_approx
define tolerance: rational = 1/1000
verify abs(sqrt2_squared - 2/1) <= tolerance

# Polynomial evaluation certificate  
define x: rational = 1/2
define poly_result: rational = x * x * x - 2/1 * x * x + x - 1/2
define expected_poly: rational = -3/8

verify poly_result == expected_poly