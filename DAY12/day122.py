import numpy as np
from scipy import stats

# Weekly Coding Hours data
data = [
    5.5, 4, 6.5, 5, 4.5, 6, 5.2, 5.8,
    4.9, 5.1, 4.8, 6.2, 5.3, 4.7, 5.6
]

# Sample statistics
sample_mean = np.mean(data)
sample_std = np.std(data, ddof=1)  # sample standard deviation
n = len(data)
degrees_freedom = n - 1

# Assume population mean (μ0) = 5 for t-test
population_mean = 5

# t-statistic
standard_error = sample_std / np.sqrt(n)
t_statistic = (sample_mean - population_mean) / standard_error

# Left-tailed p-value
p_value = stats.t.cdf(t_statistic, df=degrees_freedom)

# Output
print("Sample Mean:", sample_mean)
print("Sample Standard Deviation:", sample_std)
print("Sample Size (n):", n)
print("t-statistic:", t_statistic)
print("Degrees of Freedom:", degrees_freedom)
print("p-value (Left-tailed):", p_value)
    