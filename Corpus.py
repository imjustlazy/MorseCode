import re

test_string = '''Alice was beginning to get very tired of sitting by her sister on the bank,
 and of having nothing to do: once or twice she had peeped into the book her sister was reading, 
 but it had no pictures or conversations in it, "and what is the use of a book,"
 thought Alice "without pictures or conversation?"'''

def load_words():
	guaranty = set()
	# print(vars())
	# print(dir())
	# print(locals())
	if "test_string" in globals().keys():
		guaranty = set(re.findall(r'[a-z]+', test_string.lower()))
	print(guaranty)
	ALL = set(re.findall(r'[a-z]+', open('Data/big.txt').read().lower()))
	LONG = set(x for x in ALL if len(x) >= 4)
	CORPUS = set(re.findall(r'[a-z]+', open('Data/corpus.txt').read().lower()))
	SHORT = set(x for x in CORPUS if len(x) <= 3)
	# print(SHORT)
	return LONG | SHORT | guaranty

WORDS = load_words()

# A set of all possible prefixes of English words.
WORD_PREFIX = set(word[:j+1] for word in WORDS for j in range(len(word)))

MAX_WORD_LEN = max(l for l in set(len(word) for word in WORDS))