import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import funcs_for_stats as myst

# Task: Define several classic distributions and check CLT

# * names containing 'p_' (for pseudo) are defined using a generator
#   that yields a transform of a constant disribution to exp or gauss
names = ["Unif", "Bin", "Exp", "Norm", "p_exp", "p_norm",  "Geom", "LogN"]

def get_dist_list(sample_size):
    
    return  np.array([
        np.random.uniform(0, 1, size=sample_size),
        np.random.binomial(n=1, p=0.5, size=sample_size),
        np.random.exponential(size=sample_size),
        np.random.normal(size=sample_size),
        myst.get_list_from_dist_gen(sample_size, myst.pseudo_exp_sample),
        myst.get_list_from_dist_gen(sample_size, myst.pseudo_norm_sample),
        np.random.geometric(p=0.5, size=sample_size),
        np.random.lognormal(size=sample_size),
    ])

# define number of hist bins and samples
n_hist_bins = 21
n_sample = n_hist_bins * 101

# show the initial distributions
dist_df = pd.DataFrame(dict(zip(names, get_dist_list(n_sample))))
dist_df.hist(bins=n_hist_bins, alpha=0.5, layout = (4,2))
plt.tight_layout()
plt.show()

# <x>=0 CLT needs expectation values for each distribution
n_for_average = 500000
print(f'Averaging over {n_for_average} random variables.\n')

# print averages
dist_averages = np.mean(get_dist_list(n_for_average),axis=1)
for dist_name, avrg in zip(names, dist_averages):
    print(f'mu_{dist_name} = {avrg}')

# set number or samples and rounds
n_size_of_sample = 500
n_sums = 5000
print(f'\nSumming {n_size_of_sample} samples {n_sums} times!')

# fill the <x_i> - mu DataFrame 
sums_df = pd.DataFrame(columns = names, index = range(n_sums))
for i in range(n_sums):
    sums_df.loc[i] = np.mean(
        get_dist_list(n_size_of_sample), axis=1
        )\
        - dist_averages

# plot nice gaussians
sums_df.astype(float).hist(bins=n_hist_bins, alpha=0.5, layout = (4,2))
plt.tight_layout()
plt.show()