dimensionalArray = []
multiDimArray = []
# multiDimArray = [[0,1],[2,5],[6,7]]
cons = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
vgl = ["a","e","i","o","u","y"]

cmdExec = int(input("1 - continue | 0 - 3xi7: "))

while(cmdExec != 0):
	inpNome = input("dim - dimensionalArray | mdm - multiDimensionalArray: ")

	# Inserção de dados em array Dimensional
	if (inpNome == "dim"):
		# print("0")
		inpNome = input("Informe um nome: ")
		dimensionalArray.append(inpNome)

	# Inserção de dados em array MultiDimensional
	elif (inpNome == "mdm"):
		# print("1")
		# preencher Array MultiDimensional
		for linha in range(2):
			# inpNome = input("Informe um nome: ")
			multiDimArray.append([linha])
			for coluna in range(2):
				if (coluna == 0):
					inpNome = input("Inicio: ")
				elif (coluna == 1):
					inpNome = input("Fim: ")
				multiDimArray[linha].append(inpNome)
			print()

	# Erro	
	else:
		print("ERor")
	
	cmdExec = int(input("1 - continue | 0 - 3xi7: "))

# mostrar Array Dimensional
for dim in dimensionalArray:
	print(dim)

# mostrar Array MultiDimensional
for linha in range(len(multiDimArray)):
	for coluna in range(len(multiDimArray[linha])):
		print(multiDimArray[linha][coluna])
	print(" ")