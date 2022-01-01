letters = {
	"A": "А",
	"a": "а",
	"B": "В",
	"b": "ь",
	"C": "С",
	"c": "с",
	"E": "Е",
	"e": "е",
	"H": "Н",
	"K": "К",
	"k": "к",
	"M": "М",
	"m": "пп",
	"n": "п",
	"r": "г",
	"T": "Т",
	"t": "т",
	"W": "Ш",
	"w": "ш",
	"X": "Х",
	"x": "х",
	"Y": "У",
	"y": "у",
	"3": "З",
	"0": "О"
}

while True:
	text = input('> ')
	out = ''
	for char in text:
		out += letters[char] if char in letters else char
	print(out)