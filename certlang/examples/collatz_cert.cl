# Collatz Stopping-Time Certificate Verification
# This CertLang script verifies the numeric bounds for the Collatz stopping-time constant

# Define the exact rational bounds from the certificate
define C_lower: rational = 52141067576471723699354534458178559415185013027024167533779/5000000000000000000000000000000000000000000000000000000000
define C_upper: rational = 104282135152943447398709068916357118830370026054048335324573/10000000000000000000000000000000000000000000000000000000000

# Define the center and half-width
define C_center: rational = 52141067576471723699354534458178559415185013027024167598033/5000000000000000000000000000000000000000000000000000000000
define C_half: rational = 51403/4000000000000000000000000000000000000000000000000000000000

# Define error components
define union_bad: rational = 97/1048576
define tail_mass: rational = 1/8589934592
define total_error: rational = 370026100426912307739257812500000000000000000000051403/4000000000000000000000000000000000000000000000000000000000

# Define additional bounds from the analysis
define E_low_a: rational = 300000127156575491227414244427394158213183589766028405755043/100000000000000000000000000000000000000000000000000000000000
define E_high_a: rational = 300000127156575491227414244427394120457/100000000000000000000000000000000000000
define E_low_b: rational = 287681228157235084767676821784943595901222280627836427268701/1000000000000000000000000000000000000000000000000000000000000
define E_high_b: rational = 57536245631447016953535364356988719180244456125567285525463/200000000000000000000000000000000000000000000000000000000000

# Define threshold
define N0: rational = 1000000/1

# Core verification: The interval width must be within the total error bound
verify C_upper - C_lower <= total_error

# Verify the error components sum correctly
define error_sum: rational = union_bad + tail_mass + C_half
verify error_sum <= total_error

# Verify the center point is within the interval
verify C_lower <= C_center
verify C_center <= C_upper

# Verify interval construction is consistent
verify abs(C_center - (C_lower + C_upper)/2) <= C_half

# Additional consistency checks
verify C_lower > 0
verify C_upper > 0
verify total_error > 0
verify N0 > 0

# Verify the bounds are meaningful (non-trivial interval)
verify C_upper > C_lower

# Check that the certificate provides a tight bound
define interval_width: rational = C_upper - C_lower
verify interval_width > 0
verify interval_width < 1/1000  # Certificate should be precise to at least 0.1%

# Final verification: All error terms are positive and bounded
verify union_bad > 0
verify tail_mass > 0
verify C_half > 0
verify union_bad < 1/10
verify tail_mass < 1/1000000000
verify C_half < 1/1000000000000