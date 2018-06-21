from Morse import *
from Corpus import test_string, WORDS, MAX_WORD_LEN, WORD_PREFIX
from Encode import encode, encode_nospace
from Decode import decode, decode_nospace

print(encode(test_string))
# print(encode_nospace(test_string))

print(decode(encode(test_string)))