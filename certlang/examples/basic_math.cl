# Simple Mathematical Bounds Verification
# This example demonstrates basic rational arithmetic and bound checking

# Define some mathematical constants with rational approximations
define pi_approx: rational = 22/7
define e_approx: rational = 19/7
define golden_ratio: rational = 1618/1000

# Define some bounds for verification
define pi_lower: rational = 314/100
define pi_upper: rational = 315/100
define e_lower: rational = 27/10
define e_upper: rational = 28/10

# Verify our approximations are within reasonable bounds
verify pi_lower <= pi_approx
verify pi_approx <= pi_upper

verify e_lower <= e_approx
verify e_approx <= e_upper

# Test some mathematical properties
verify golden_ratio > 1
verify golden_ratio < 2

# Verify some arithmetic properties
define sum_test: rational = 1/2 + 1/3
define expected_sum: rational = 5/6
verify sum_test == expected_sum

# Test absolute value function
define negative_val: rational = -5/3
verify abs(negative_val) == 5/3

# Test max and min functions
verify max(1/2, 3/4) == 3/4
verify min(1/2, 3/4) == 1/2

# Test interval arithmetic
define test_interval: interval = interval(1/3, 2/3)
verify width(test_interval) == 1/3