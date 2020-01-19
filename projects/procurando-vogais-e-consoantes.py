wordSlb = []
sepSlb = []

word = "BARUERI"

# cons = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
cons = ["b", "c", "d", "f", "k","r"]
vog = ["a", "e", "i", "u"]
c = []
v = []

lenSW = 0
for linhaSilaba in range(len(word)):
	for colunaSilaba in range(1):
		
		for consProc in range(len(cons)):
			# print(str(word[linhaSilaba]) + " == " + str(cons[consProc].upper()))
			
			# igual a consoante inicio
			if (word[linhaSilaba] == cons[consProc].upper()):
				# print("encontrei um " + str(word[linhaSilaba]) + " na posicao --> " + str(linhaSilaba))
				c.append(linhaSilaba)
				lenSW += 1

		for vogProc in range(len(vog)):
			if (word[linhaSilaba] == vog[vogProc].upper()):
				print("encontrei um " + str(word[linhaSilaba]) + " na posicao --> " + str(linhaSilaba))
				v.append(linhaSilaba)
				lenSW += 1
v.pop(1)
print(v)

# for linhaSW in range(lenSW):
for linhaSW in range(3):
	# for colunaSilaba in range(2):
	for colunaSW in range(2):
		if (colunaSW == 0):
			sepSlb.append([linhaSW])
			sepSlb[linhaSW].append(c[linhaSW])
			sepSlb[linhaSW].append(v[linhaSW])

print(sepSlb)
print(lenSW)