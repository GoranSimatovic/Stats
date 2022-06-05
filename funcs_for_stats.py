import numpy as np
import pandas as pd
import random

def get_list_from_dist_gen(n, gen):

    output_list = []
    for i in range(n):
        output_list.append(next(gen()))

    return output_list


# Cosine Box-Muller generator
def pseudo_norm_sample():

    yield np.sqrt(-2 * np.log(np.random.uniform(0, 1))) * np.cos(
        2 * np.pi * np.random.uniform(0, 1)
    )


def pseudo_exp_sample():

    yield -np.log(np.random.uniform(0, 1))



def get_sampled(n_samples, sub_sample_size, population_df):
    sub_sample_observations = pd.DataFrame(
        columns=['average', 'st_dev'], index=range(n_samples)
    )

    for i in range(n_samples):
        sub_range = population_df.loc[
            random.sample(range(len(population_df)),
                          sub_sample_size), 'observations'
        ]
        sub_sample_observations.loc[i] = [sub_range.mean(), sub_range.std()]

    return sub_sample_observations.astype(float)