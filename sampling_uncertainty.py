import numpy as np
import pandas as pd
import random
from matplotlib import pyplot as plt
from scipy.stats import norm
import funcs_for_stats as myst

population_size = 50000
population_df = pd.DataFrame(
    {'observations': np.random.normal(size=population_size)})

n_samples = 500
sub_sample_size = 500
sub_sample_observations = pd.DataFrame(
    columns=['average', 'st_dev'], index=range(n_samples)
)


n_bins = 50
width = 0.3

kwargs_mean = {'alpha': 0.5,
               'bins': np.linspace(-width, width, n_bins),
               'density': True,
               'histtype': 'bar',
               'stacked': True,
               }
kwargs_std = {'alpha': 0.5,
              'bins': np.linspace(1-width, 1+width, n_bins),
              'density': True,
              'histtype': 'bar',
              'stacked': True,
              }

kwargs_list = [kwargs_mean, kwargs_std]

n_samples = 5000
multiplier = 9
sample_size = 300
sample_sizes = [sample_size, multiplier*sample_size]

samples = [myst.get_sampled(n_samples, sample_sizes[x], population_df)
           for x in range(len(sample_sizes))]



fig, axes = plt.subplots(2, 2)

data_names = ['small', 'big']
for i, feature in enumerate(['average', 'st_dev']):
    for j, data_sample in enumerate(samples):
        ax = axes[j][i]
        ax.hist(data_sample[feature], **kwargs_list[i])
        ax.set_title(f'Plot ({feature}, {data_names[j]})')
        mean = round(data_sample[feature].mean(), 4)
        sigma = round(data_sample[feature].std(), 4)
        y = norm.pdf(kwargs_list[i].get("bins"), mean, sigma)
        if i % 2 == 0:
            ax.set_title(f'P($\mu$, N = {sample_sizes[j]})')
            ax.plot(kwargs_list[i].get("bins"),
                    y,
                    'b--',
                    linewidth=1,
                    )
            ax.text(0.05, 0.9,
                    f'$\mu_\mu$ = {mean}\n$\sigma_\mu$ = {sigma}',
                    horizontalalignment='left',
                    verticalalignment='top',
                    transform=ax.transAxes)
        else:
            ax.set_title(f'P($\sigma$, N = {sample_sizes[j]})')
            ax.plot(kwargs_list[i].get("bins"),
                    y,
                    'b--',
                    linewidth=1,
                    )
            ax.text(0.05, 0.9,
                    f'$\mu_\sigma$ = {mean}\n$\sigma_\sigma$ = {sigma}',
                    horizontalalignment='left',
                    verticalalignment='top',
                    transform=ax.transAxes)
plt.tight_layout()
plt.show()
