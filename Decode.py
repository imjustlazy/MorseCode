from Morse import MORSE_DECODE, MAX_CODE_LEN
from Corpus import WORDS, MAX_WORD_LEN, WORD_PREFIX
import re
import pdb

min_words_list = []

def try_reconginize(words_saw , char_left):
    """
    print lists of possible word-list from a list of characters
    """
    # print("\nin trying: words_saw:", words_saw, "\nchar_left:", char_left)
    global min_words_list
    if len(char_left) == 0:
        # print("renew the answer!!!!!!")
        if len(words_saw) < len(min_words_list):
            min_words_list = words_saw.copy()
        return
    for i in range(min(len(char_left), MAX_WORD_LEN), 0, -1):
        if char_left[:i] in WORDS:
            words_saw.append(char_left[:i])
            try_reconginize(words_saw, char_left[i:])
            words_saw.pop()


def decode(code_string):
    """
    returns a list of possible decode ways
    every word in every candidate word-list truly exists
    """
    global min_words_list
    # code_string may contains more spaces if non-alphabet exists in original txt_string, both of next two lines work
    # code_list = re.split(r" +", code_string)[:-1]
    # code_list = list(filter(lambda x: x != "", code_string.split(" ")))
    # changed encode() so above situation won't emerge, do that simply in the way below
    characters = "".join([MORSE_DECODE[code] for code in code_string.split(" ")])
    print(characters)
    min_words_list = list(characters)
    # pdb.set_trace()
    try_reconginize([], characters)
    print(min_words_list, len(min_words_list))


def decode_nospace(words_saw, chars_saw, code_left):
    """
    this should be a recursive function
    words_saw: list, thw words list recognized, every word truly exists
    chars_saw: string, the characters list recognizes, should be prefix of a word
    code_left: string, the morse code left
    """
    # print("words_saw:", words_saw, "chars_saw:", chars_saw, "code_left:", code_left)
    if len(code_left) == 0:
        if chars_saw in WORDS:
            words_saw.append(chars_saw)
            print(words_saw)
        return
    if len(chars_saw) > MAX_WORD_LEN:
        return
    if len(words_saw) > 2 and words_saw[-1] == words_saw[-2]:
        return
    if len(words_saw) > 4 and len("".join(words_saw[-7:])) < 15:
        return
    if chars_saw in WORDS:
        words_saw.append(chars_saw)
        decode_nospace(words_saw, "", code_left)
        words_saw.pop()
    for length in range(1, min(len(code_left), MAX_CODE_LEN) +1):
        if code_left[:length] in MORSE_DECODE:
            tmpchars = chars_saw + MORSE_DECODE[code_left[:length]]
            if tmpchars in WORD_PREFIX:
                decode_nospace(words_saw, tmpchars, code_left[length:])
