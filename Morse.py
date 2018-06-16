
# only contains alphabet now

CODES = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....',
		'..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.',
		'--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-',
		'-.--', '--..']

ALPHABETS = "abcdefghijklmnopqrstuvwxyz"

MORSE_ENCODE = dict(zip(ALPHABETS, CODES))

MORSE_DECODE = dict(zip(CODES, ALPHABETS))

MAX_CODE_LEN = 4

CODE_PREFIX = set(code[:j+1] for code in CODES for j in range(len(code)))