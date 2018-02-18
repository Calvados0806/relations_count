# Global variables
counter = 0
d = set()

# Some needed functions
def rem(T, e):
	T1 = list(T)
	T1.remove(e)
	return tuple(T1)

def P(S, l):
	for i in range(l):
		if l != 2:
			if S[i] not in d:
				d.add(tuple(S[i]))
			if rem(S, S[i]) not in d:
				d.add(tuple(rem(S, S[i])))
			if P(rem(S, S[i]), l - 1) not in d:
				d.add(P(rem(S, S[i]), l - 1))
		else:
			return S

def isTransit(T):
	global counter
	bool1 = True
	if T == None:
		counter += 1
	if type(T) == tuple and len(T) == 2 and type(T[0]) == str:
		counter += 1
	if type(T) == tuple and len(T) > 1 and type(T[0]) == tuple:
		for i in T:
			temp = False
			if i[0] == i[1]:
				continue
			else:
				for k in T:
					if i[1] == k[0]:
						temp = True
				if not temp:
					continue
			for j in T:
				if i != j:
					if i[1] == j[0]:
						if (i[0], j[1]) in T:
							pass
						else:
							bool1 = False
		if bool1:
			counter += 1

# Main code
def main():
	global d
	global counter
	a, b, c = 'a', 'b', 'c'
	m = (a, b, c)
	dec = list()

	for i in range(len(m)):
		for j in range(len(m)):
			dec.append((m[i], m[j]))

	length = len(dec)
	d.add(None)
	d.add(tuple(dec))
	P(tuple(dec), length)
	d = tuple(d)

	for i in d:
		isTransit(i)

	print(counter)

if __name__ == '__main__':
	main()
