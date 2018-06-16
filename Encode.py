from Morse import MORSE_ENCODE

def encode(txt_string):
    """
    returns a string
    standard type of morse code (with space as delimiter)
    ignore non-alphabet in input txt_string
    """
    txt_string = txt_string.lower().replace(" ", "")
    code_list = []
    for c in txt_string:
        # auto ingore characters not alphabet
        code_list.append(MORSE_ENCODE.get(c, ""))
    return " ".join(code_list)

def encode_nospace(txt_string):
    """
    returns a string
    no space in between as delimiter
    """
    return encode(txt_string).replace(" ", "")