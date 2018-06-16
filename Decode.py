from Morse import MORSE_DECODE
from Corpus import WORDS, MAX_WORD_LEN

def try_reconginize(words_saw , char_left):
    """
    print lists of possible word-list from a list of characters
    """
    if len(char_left) == 0:
        print(words_saw)
        return
    for i in range(min(len(char_left), MAX_WORD_LEN)):
        if char_left[:i+1] in WORDS:
            words_saw.append(char_left[:i+1])
            try_reconginize(words_saw, char_left[i+1:])


def decode(code_string):
    """
    returns a list of possible decode ways
    every word in every candidate word-list truly exists
    """
    code_list = code_string.split(" ")
    characters = ""
    for code in code_list:
        characters += MORSE_DECODE[code]
    print(characters)
    # candidate_answers = []
    try_reconginize([], characters)
    # return candidate_answers