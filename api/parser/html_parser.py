
def parse(raw):
	depth = 0
	start = 0
	pairs = []
	for idx, ch in enumerate(raw):
		if ch == '<':
			depth += 1
			if depth == 1:
				pairs.append([start, idx])
		elif ch == '>':
			depth -= 1
			if depth <= 0 and start == -1:
				start = idx

	res = []

	for pair in pairs:
		if pair[1] - pair[0] >= 10:
			res.append(pair)

	return res

if __name__ == '__main__':
	raw = open('test.htm', 'r').read()
	p = parseHTML(raw)
		
