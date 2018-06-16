import re

def load_words():
	ALL = set(re.findall(r'[a-z]+', open('big.txt').read().lower()))
	LONG = set(x for x in ALL if len(x) > 3)
	CORPUS = set(re.findall(r'[a-z]+', open('corpus.txt').read().lower()))
	SHORT = set(x for x in CORPUS if len(x) < 4)
	return LONG | SHORT

WORDS = load_words()

# A set of all possible prefixes of English words.
WORD_PREFIX = set(word[:j+1] for word in WORDS for j in range(len(word)))

MAX_WORD_LEN = max(l for l in set(len(word) for word in WORDS))