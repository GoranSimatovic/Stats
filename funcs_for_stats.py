import numpy as np

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