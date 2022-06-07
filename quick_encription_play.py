import string


def ceaser_cypher_a_string(input_string, shift_size):

    def ceasers_shift(letter, shift_size):

        assert type(letter) == str, 'Input not a string!'
        assert len(letter) == 1, 'Input not a single letter!'

        first_alphabet = list(string.ascii_lowercase)
        cypher_dict = dict(zip(
            first_alphabet,
            first_alphabet[shift_size:] +
            first_alphabet[:shift_size]
        ))

        if letter.lower() in cypher_dict:
            return cypher_dict[letter.lower()]
        else:
            return letter

    return ''.join([ceasers_shift(x, shift_size) for x in input_string])



if __name__ == '__main__':

    shift = 4  # Caesar did A->D shift
    text = 'hello world'


    print(f'The input message is:\n' +
        text
        )

    print(f'The encrypted message is:\n' +
        ceaser_cypher_a_string(text, -shift)
        )

    print(f'The decrypted message is:\n' +
        ceaser_cypher_a_string(
            ceaser_cypher_a_string(text, shift),
            -shift)
        )

    do_alphabet_test = True

    if do_alphabet_test:

        print('Performing aphabet test:\n' +
            ceaser_cypher_a_string(
                ceaser_cypher_a_string(string.ascii_lowercase, shift),
                -shift))