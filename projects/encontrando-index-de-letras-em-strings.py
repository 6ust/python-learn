wordSlb = []
sepSlb = []

word = "BARUERI"

cons = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]


letraProc = input("Sua palavra é " + word + ", informe a LETRA a ser procurada: ")

for linhaSilaba in range(len(word)):
	sepSlb.append([linhaSilaba])
	for colunaSilaba in range(2):
		if (colunaSilaba == 0):
			print("coluna " + str(0))
			print(word[linhaSilaba])
			if (word[linhaSilaba] == letraProc.upper()):
				print("encontrei um " + str() + " na posicao --> " + str(linhaSilaba))

		# igual a vogal fim
		elif (colunaSilaba == 1):
			print("coluna " + str(1))

	print()

print(sepSlb)