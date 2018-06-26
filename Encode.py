from Morse import MORSE_ENCODE, ALPHABETS

def encode(txt_string):
    """
    returns a string
    standard type of morse code (with space as delimiter)
    ignore non-alphabet in input txt_string
    """
    code_list = [MORSE_ENCODE[c] for c in txt_string.lower() if c in ALPHABETS]
    code_string = " ".join(code_list)
    return code_string

def encode_nospace(txt_string):
    """
    returns a string
    no space in between as delimiter
    """
    return encode(txt_string).replace(" ", "")