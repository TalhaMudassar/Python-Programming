import numpy as np
from scipy import stats

# Sample data
data = [
    2.548685661, 2.29469428, 2.609075415, 2.959211943, 2.25633865,
    2.256345217, 2.981685126, 2.656973892, 2.162210246, 2.567024017,
    2.164632923, 2.163708099, 2.446784909, 1.584687902, 1.660032867,
    2.125084988, 1.944867552, 2.475698933, 1.98679037, 1.785078519,
    2.936259508, 2.25968948, 2.377011282, 1.780100726, 2.13224691,
    2.394369036, 1.889602569, 2.500279207, 2.109744524, 2.2333225,
    2.109317355, 3.090911274, 2.34460111, 1.926915628, 2.679017965,
    1.86166254, 2.433545438, 1.56613195, 1.81872558, 2.428744494,
    2.645386632, 2.418547312, 2.303740687, 2.229558522, 1.758591204,
    2.062062317, 2.165744492, 2.77284889, 2.487447316, 1.644783938
]

# Sample mean
sample_mean = np.mean(data)

# Assume population mean = 2
population_mean = 2
sample_std = np.std(data, ddof=1)
n = len(data)
standard_error = sample_std / np.sqrt(n)
z_statistic = (sample_mean - population_mean) / standard_error

# p-value (two-tailed)
p_value = 2 * (1 - stats.norm.cdf(abs(z_statistic)))

print("Sample Mean:", sample_mean)
print("Z-Statistic:", z_statistic)
print("P-Value:", p_value)
