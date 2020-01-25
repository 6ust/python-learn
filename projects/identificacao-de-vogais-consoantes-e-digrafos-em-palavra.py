# PALAVRA TESTE
# word = "DESÇAM"
# word = "BARUERI"
word = input("Informe uma palavra:")
word = word.upper()
# CONTADORES
counterWord = 1

# ARRAY DE INDEX
consonantId = []
vowelId = []
digraphId = []

# ARRAY DE SILABAS
wordSyllableSep = separatorSyllable = []


# --------------------------------------------
# REGRAS DE SEPARAÇÃO DE SILABA
# --------------------------------------------
# SEPARAR QUANDO
digraphs = ["rr", "ss", "sc", "sç", "xc"]
consonant = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z", "ç"]
vowel = ["a", "e", "i", "o" , "u", "y"]

# NÃO SEPARAR QUANDO

# ********************************************

print("\n\n\n")
print("----------------------------------------------------")
print("--- SEPARAÇÃO DE CONSOANTES/ VOGAIS/ DIGRAFOS ------")
print("----------------------------------------------------")

print("\n")
print("PALAVRA => " + word)
print("\n")

# --------------------------------------------
# ANALISE INDEX DE SEPARAÇÃO
# --------------------------------------------
lenSyllableWord = 0


for lineSyllable in range(len(word)):
	for columnSyllable in range(1):

		# PERCORRE ARRAY DE ANALISE DE digraphs
		for digraphsSearchAdjust in range(len(digraphs)):
			# REGRA PARA NÃO LER A MAIS, [M_] POSIÇÃO NÃO EXISTENTE 
			if lineSyllable < (len(word) - 1):

				# IGUAL A DIGRAFO INICIO
				if (word[lineSyllable:][:2] == digraphs[digraphsSearchAdjust].upper()):
					digraphId.append(lineSyllable)
					print("Digrafo encontrado -> " + str(word[lineSyllable:][:2]))

		# PERCORRE ARRAY DE ANALISE DE CONSOANTES
		for consonantSearch in range(len(consonant)):
			
			# IGUAL A CONSOANTE INICIO
			if (word[lineSyllable] == consonant[consonantSearch].upper()):
				consonantId.append(lineSyllable)
				print("Consoante encontrada -> " + str(word[lineSyllable]))
				# lenSyllableWord += 1

		# SEPARADOR DE VOGAIS
		for vowelSearch in range(len(vowel)):

			# IGUAL A VOGAL INICIO
			if (word[lineSyllable] == vowel[vowelSearch].upper()):
				vowelId.append(lineSyllable)
				print("Vogal encontrada -> " + str(word[lineSyllable]))
				# lenSyllableWord += 1

# ********************************************

# --------------------------------------------
# ORGANIZAÇÃO DE SEPARAÇÃO DE SILABAS - REGRA
# --------------------------------------------




# ------------------------------------------------
# VISUALIZAÇÃO DE INDEX PARA REALIZAÇÃO DE TESTES
# ------------------------------------------------
print("\n\n\n\n")
print("===================================")
print("=== ORGANIZAÇÃO ===================")
print("===================================")

print("DIGRAPHS ==> " + str(digraphId))
print("VOWEL ==> " + str(vowelId))
print("CONSONANT ==> " + str(consonantId))



print()
print()

# ORGANIZADOR DE SEPARAÇÃO DE SILABAS



# MOSTRAR RESULTADO
# for lineShow in range(lenSyllableWord):
# 	for columnShow in range(1):
# 		print( word[lineShow :] [:2] )