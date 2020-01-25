# Author: Gustavo Guedes - 6ust <- [Git]

def jumpLine(amount):
	counterAmount = 0
	while(counterAmount < amount):
		print()
		counterAmount += 1

# PALAVRA TESTADA
# word = "DESÇAM"
# word = "BARUERI"


# PALAVRA TESTE
# word = "AMOR"
# word = "LEAO"
# word = "CAMALEAO"

# PALAVRA A ESCOLHA DO USUARIO
word = input("\n\nInforme uma palavra padrao de palavras aceitas: \nNAO COMECE COM VOGAL \nNAO SEJA PLURAL \nNAO TERMINE COM CONSOANTE:\n")
word = word.upper()


# CONTADORES
counterWord = 1

# ARRAY DE INDEX
consonantId = []
vowelId = []
digraphId = []

# ARRAY DE SILABAS
wordSyllableSep = []
separatorSyllableIds = []


# --------------------------------------------
# REGRAS DE SEPARAÇÃO DE SILABA
# --------------------------------------------
# SEPARAR QUANDO
digraphs = ["rr", "ss", "sc", "sç", "xc"]
consonant = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z", "ç"]
vowel = ["a", "e", "i", "o" , "u", "y"]

# NÃO SEPARAR QUANDO

# ********************************************

jumpLine(1)
print("---------------------------------")
print("--- AMBIENTE DE TESTES 002 ------")
print("---------------------------------")

jumpLine(1)
print("PALAVRA => " + word)
jumpLine(1)

# --------------------------------------------
# ANALISE INDEX DE SEPARAÇÃO
# --------------------------------------------
lenSyllableWord = 0

# PERCORRE ARRAY [WORD]
for lineWord in range(len(word)):
	for columnWord in range(1):

		# PERCORRE ARRAY DE ANALISE DE digraphs
		for digraphsSearchAdjust in range(len(digraphs)):
			# REGRA PARA NÃO LER A MAIS, [M_] POSIÇÃO NÃO EXISTENTE 
			if lineWord < (len(word) - 1):

				# IGUAL A DIGRAFO INICIO
				if (word[lineWord:][:2] == digraphs[digraphsSearchAdjust].upper()):
					digraphId.append(lineWord)
					print("Digrafo encontrado -> " + str(word[lineWord:][:2]))

		# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

		# PERCORRE ARRAY DE ANALISE DE CONSOANTES
		for consonantSearch in range(len(consonant)):
			
			# IGUAL A CONSOANTE INICIO
			if (word[lineWord] == consonant[consonantSearch].upper()):
				consonantId.append(lineWord)
				print("Consoante encontrada -> " + str(word[lineWord]))
				# lenSyllableWord += 1

		# SEPARADOR DE VOGAIS
		for vowelSearch in range(len(vowel)):

			# IGUAL A VOGAL INICIO
			if (word[lineWord] == vowel[vowelSearch].upper()):
				vowelId.append(lineWord)
				print("Vogal encontrada -> " + str(word[lineWord]))
				# lenSyllableWord += 1

		# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# --------------------------------------------
# REMOVENDO REPETIÇÃO DE VOGAIS
# --------------------------------------------
for vowelIndex in range(len(vowelId)):
	if (vowelIndex < len(vowelId) - 1):
		# print(str(vowelId[vowelIndex + 1]) + " - " + str(vowelId[vowelIndex]) + " = " + str((vowelId[vowelIndex + 1] - vowelId[vowelIndex])) + " ====>" + str((vowelId[vowelIndex + 1] - vowelId[vowelIndex]) == 1))
		if (vowelId[vowelIndex + 1] - vowelId[vowelIndex]) == 1:
			vowelId.pop(vowelIndex)

# ********************************************

			
# --------------------------------------------
# GERAR SILABAS DA PALAVRA
# --------------------------------------------
jumpLine(1)
print("-------------------------------------------------------------------------")
print("--- Gerando silaba da palavra --> " + str(word))
print("-------------------------------------------------------------------------")
jumpLine(1)

# CASO A PALAVRA NAO COMECE COM VOGAL/ NAO SEJA PLURAL/ NAO TERMINE COM CONSOANTE
if (len(consonantId) == len(vowelId)):
	for consonantIndex in range(len(consonantId)):	
		print("incluindo intervalo de sílaba ------> [ " + str(consonantId[consonantIndex]) + " - " + str(vowelId[consonantIndex]) + " ]")
		for startAndEnd in range(2):
			if startAndEnd == 0:
				separatorSyllableIds.append([consonantIndex])
				separatorSyllableIds[consonantIndex].append(consonantId[consonantIndex])
				separatorSyllableIds[consonantIndex].append((vowelId[consonantIndex] - consonantId[consonantIndex]) + 1)
	jumpLine(1)


# else:
# 	for vowelIndex in range(len(vowelId)):
# 		print("Incl V ------>" + str(consonantId[vowelIndex]) + " - " + str(vowelId[vowelIndex]))
# 		separatorSyllableIds.append(vowelId[vowelIndex])
# 		# separatorSyllableIds.append(consonantId[consonantIndex])

print("SEPARATOR SYLLABLE IDS ==> " + str(separatorSyllableIds))
jumpLine(1)
print("****************************************")
# ********************************************


# -----------------------------------------------------
# VIZUALIZAÇÃO DE INDEXES PARA REALIZAÇÃO DE TESTES
# -----------------------------------------------------

# jumpLine(1)
# print("CONSONANTS")
# print(consonantId)

# jumpLine(1)
# print("VOWELS")
# print(vowelId)

# ********************************************


# --------------------------------------------
# ORGANIZAÇÃO DE SEPARAÇÃO DE SILABAS - REGRA
# --------------------------------------------
# for consonantIndex in range(len(consonantId)):
# 	print("CONS --------> "  + str(word[consonantId[consonantIndex]]))
# 	for vowelIndex in range(len(vowelId)):
# 		print("VOG ---> "  + str(word[vowelId[vowelIndex]]))
# 		print()
# 		# separatorSyllableIds.append(consonantIndex)


# ********************************************


# ------------------------------------------------
# VISUALIZAÇÃO DE INDEX PARA REALIZAÇÃO DE TESTES
# ------------------------------------------------
jumpLine(2)
print("===================================")
print("=== ORGANIZAÇÃO ===================")
print("===================================")
jumpLine(1)

print("DIGRAPHS ==> " + str(digraphId))
print("VOWEL ==> " + str(vowelId))
print("CONSONANT ==> " + str(consonantId))
jumpLine(1)
print("SEPARATOR SYLLABLE IDS ==> " + str(separatorSyllableIds))
jumpLine(1)
print("****************************************")

# print("SEPARATOR LEN ==> " + str(len(separatorSyllableIds)))

# VISUALIZAÇÃO DAS SILABAS
jumpLine(1)
print("---------------------------------")
print("--- VISUALIZAÇÃO DE SEPARAÇÃO ---")
print("---------------------------------")
jumpLine(1)
print(word)
jumpLine(1)

for separatorSyllableIndex in range(len(separatorSyllableIds)):	
	for startAndEnd in range(1):
		print(str( word[ separatorSyllableIds[separatorSyllableIndex][1] :] [: (separatorSyllableIds[separatorSyllableIndex][2])] ))
		# print("COLUNA" + str(separatorSyllableIds[separatorSyllableIndex][2]))
		# print( word[separatorSyllableIndex :] [: startAndEnd] )

print("****************************************")