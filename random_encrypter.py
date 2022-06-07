
import enum
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import re
import string
from quick_encription_play import caeser_cypher_a_string as caesar


# A short example of how to stop frequency analysis in a Caesar shift algorithm
# - final output has a flat frequency distribution


if __name__ == '__main__':

    file_location = 'text_sample.txt'
    with open(file_location, 'r') as f:
        text = re.sub('[^a-zA-Z ]', '', f.read()).lower()


    words = pd.DataFrame({'words':text.split(' ')})
    shifted_words = pd.DataFrame({'words' : [caesar(x,4) for x in words.words]})
    
    letters = pd.DataFrame({'letters' : [x for x in text if x.isalnum()]})
    shifted_letters = pd.DataFrame({'shifted letters' : [caesar(x,4) for x in letters.letters]})

    shifting_key = np.random.randint(0,26, len(text))
    random_shifted_letters = pd.DataFrame({'shifted letters' : [caesar(x,shifting_key[i]) for i,x in letters.letters.items()]})

    
    letter_frequencies = letters.value_counts().sort_index()
    shifted_letter_frequencies = shifted_letters.value_counts().sort_index()
    random_shifted_letters_frequencies = random_shifted_letters.value_counts().sort_index()


    names = ['Regular text', 'Caesar shifted (+4) text', 'Random shifted text']
    frequencies = [letter_frequencies, 
                   shifted_letter_frequencies, 
                   random_shifted_letters_frequencies,
    ]

    x = np.arange(26)
    width = 0.3

    fig, axes = plt.subplots(3)

    for idx, frequency in enumerate(frequencies):
        ax = axes[idx]
        ax.bar(x, frequency)
        ax.set_xticks(x)
        ax.set_title(names[idx])
        ax.set_xticklabels(list(string.ascii_lowercase))
    
    plt.tight_layout()
    plt.show()