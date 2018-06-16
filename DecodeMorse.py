import re
# from collections import Counter

message = """
.-.-....-.-...--.-...-....--...-.-...-.--.------..-...-..-.-.---...-..-..---..-..
....--..-.--.-...-.--......-.........-..-.----.-.....-....--.-.-.--.-..---..-....
..-...-..-.--.-.----......-.--.-----..-------.-.-..---.-.-.--..-.-...............
--...--....--..-....-.-----.....-...-------.-......-.........-..-..--.-....-...--
....-.--.-.....--..-.....--..-.---.--...-.-.-..-.-.....---.-.-.-.----....-..-....
.--..----......-...-.--.-...--.....--.....-.......-....---..-..--...-------.--...
.---..---.....-.-.-....-.-...--..-....---..--.--...-.-.-..-.-.....---.-.-.-.----.
...-..-.....--..----.""".replace("\n", "")

CODES = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....',
		'..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
		'--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-',
		'-.--', '--..']

ALPHABETS = "abcdefghijklmnopqrstuvwxyz"

MORSE_ENCODE = dict(zip(ALPHABETS, CODES))

MORSE_DECODE = dict(zip(CODES, ALPHABETS))

MAX_CODE_LEN = 4

def try_reconginize(words_saw , char_left):
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
	every word in every candidate word list truly exists
	"""
	code_list = code_string.split(" ")
	characters = ""
	for code in code_list:
		characters += MORSE_DECODE[code]
	print(characters)
	# candidate_answers = []
	try_reconginize([], characters)
	# return candidate_answers


def load_words():
	ALL = set(re.findall(r'[a-z]+', open('big.txt').read().lower()))
	LONG = set(x for x in ALL if len(x) > 3)
	CORPUS = set(re.findall(r'[a-z]+', open('corpus.txt').read().lower()))
	SHORT = set(x for x in CORPUS if len(x) < 4)
	return LONG | SHORT

WORDS = load_words()

# A set of all possible prefixes of English words.
PREFIXES = set(word[:j+1] for word in WORDS for j in range(len(word)))

MAX_WORD_LEN = max(l for l in set(len(word) for word in WORDS))

# or named decode_nospace
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
	if len(words_saw) > 4 and len("".join(words_saw[-5:])) < 10:
		return
	if chars_saw in WORDS:
		words_saw.append(chars_saw)
		decode_nospace(words_saw, "", code_left)
		words_saw.pop()
	for length in range(1, min(len(code_left), MAX_CODE_LEN) +1):
		if code_left[:length] in MORSE_DECODE:
			tmpchars = chars_saw + MORSE_DECODE[code_left[:length]]
			if tmpchars in PREFIXES:
				decode_nospace(words_saw, tmpchars, code_left[length:])

print(decode_nospace([], "", message))

def encode(txt_string):
	txt_string = txt_string.lower().replace(" ", "")
	code_list = []
	for c in txt_string:
		code_list.append(MORSE_ENCODE.get(c, ""))
	return " ".join(code_list)

def encode_nospace(txt_string):
	return encode(txt_string).replace(" ", "")


test_string = 'Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice "without pictures or conversation?"'

print(encode(test_string))
print(encode_nospace(test_string))

output = """.-.-....-.-...--.-...-....--...-.-...-.--.------..-...-..-.-.---...-..-..---..-......--..-.--.-...-.--......-.........-..-.----.-.....-....--.-.-.--.-..---..-......-...-..-.--.-.----......-.--.-----..-------.-.-..---.-.-.--..-.-...............--...--....--..-....-.-----.....-...-------.-......-.........-..-..--.-....-...--....-.--.-.....--..-.....--..-.---.--...-.-.-..-.-.....---.-.-.-.----....-..-.....--..----......-...-.--.-...--.....--.....-.......-....---..-..--...-------.--....---..---.....-.-.-....-.-...--..-....---..--.--...-.-.-..-.-.....---.-.-.-.----....-..-.....--..----."""

print(decode(encode(test_string)))
print(decode_nospace([], "", encode_nospace(test_string)))

print(decode_nospace([], "", message))

# def break_words(input, S, W, C):
#     while True:
#         if not input:
#             if W == C == '':
#                 yield S
#             return
#         i, input = input[0], input[1:]
#         C += i
#         if not is_morse_prefix(C):
#             return
#         ch = DEMORSE.get(C, None)
#         if ch is None or not is_word_prefix(W + ch):
#             continue
#         for result in break_words(input, S, W + ch, ''):
#             yield result
#         if is_word(W + ch):
#             for result in break_words(input, S.append(' ' + W + ch), '', ''):
#                 yield result

# for S in break_words(mymsg, [], '', ''):
#     print(S)




# def translate(msg, c_sep=' ', w_sep=' / '):
#     """Turn a message (all-caps space-separated words) into morse code."""
#     return w_sep.join(c_sep.join(MORSE[c] for c in word)
#                       for word in msg.split(' '))

# def encode(msg):
#     """Turn a message into timing-less morse code."""
#     return translate(msg, '', '')

# def c_trans(morse):
#     """Construct a map of char transitions.

#     The return value is a dict, mapping indexes into the morse code stream
#     to a dict of possible characters at that location to where they would go
#     in the stream. Transitions that lead to dead-ends are omitted.
#     """
#     result = [{} for i in range(len(morse))]
#     for i_ in range(len(morse)):
#         i = len(morse) - i_ - 1
#         for c, m in MORSE.items():
#             if i + len(m) < len(morse) and not result[i + len(m)]:
#                 continue
#             if morse[i:i+len(m)] != m: continue
#             result[i][c] = i + len(m)
#     return result

# def find_words(ctr, i, prefix=''):
#     """Find all legal words starting from position i.

#     We generate all possible words starting from position i in the
#     morse code stream, assuming we already have the given prefix.
#     ctr is a char transition dict, as produced by c_trans.
#     """
#     if prefix in WORDS:
#         yield prefix, i
#     if i == len(ctr): return
#     for c, j in ctr[i].items():
#         if prefix + c in PREFIXES:
#             for w, j2 in find_words(ctr, j, prefix + c):
#                 yield w, j2

# def w_trans(ctr):
#     """Like c_trans, but produce a word transition map."""
#     result = [{} for i in range(len(ctr))]
#     for i_ in range(len(ctr)):
#         i = len(ctr) - i_ - 1
#         for w, j in find_words(ctr, i):
#             if j < len(result) and not result[j]:
#                 continue
#             result[i][w] = j
#     return result

# def shortest_sentence(wt):
#     """Given a word transition map, find the shortest possible sentence.

#     We find the sentence that uses the entire morse code stream, and has
#     the fewest number of words. If there are multiple sentences that
#     satisfy this, we return the one that uses the smallest number of
#     characters.
#     """
#     result = [-1 for _ in range(len(wt))] + [0]
#     words = [None] * len(wt)
#     for i_ in range(len(wt)):
#         i = len(wt) - i_ - 1
#         for w, j in wt[i].items():
#             if result[j] == -1: continue
#             if result[i] == -1 or result[j] + 1 + len(w) / 30.0 < result[i]:
#                 result[i] = result[j] + 1 + len(w) / 30.0
#                 words[i] = w
#     i = 0
#     result = []
#     while i < len(wt):
#         result.append(words[i])
#         i = wt[i][words[i]]
#     return result

# def sentence_count(wt):
#     result = [0] * len(wt) + [1]
#     for i_ in range(len(wt)):
#         i = len(wt) - i_ - 1
#         for j in wt[i].values():
#             result[i] += result[j]
#     return result[0]

# msg = 'JACK AND JILL WENT UP THE HILL'
# print(sentence_count(w_trans(c_trans(encode(msg)))))
# print(shortest_sentence(w_trans(c_trans(encode(msg)))))

