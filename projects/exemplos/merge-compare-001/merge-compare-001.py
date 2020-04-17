import os

# CAMINHO DOS DIRETORIOS
pathDefault = "."
path1 = pathDefault + "\\t1\\"
path2 = pathDefault + "\\t2\\"


# LISTA DE NOME DOS ARQUIVOS DO DIRETORIO
lstFiles1 = []
lstFiles2 = []

# CONTADORES DE NAO EXISTENCIA
countNotExistInPath1 = 0
countNotExistInPath2 = 0

# LISTA DE NOVOS E EXISTENTES
newInLstFiles1     = []
newInLstFiles2     = []
existInBothLsts    = []

# LISTA FINAL DOS EXISTENTES
# [NOME ARQUIVO, LINHAS FALTANTES, DIFERENCAS, FALTANTES + DIFERENCAS]
finalArrayOfExisting = []


# >>>>>>>>>>>> AREA DE LISTAGEM DE DIRETORIO <<<<<<<<<<<<

# LISTAGEM DE ARQUIVOS DE UM DIRETORIO
for r, d, f in os.walk(path1):
	for file in f:
		if "" in file:
			lstFiles1.append(os.path.join(r, file)[len(path1):])

for r, d, f in os.walk(path2):
	for file in f:
		if "" in file:
			lstFiles2.append(os.path.join(r, file)[len(path1):])

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||


# >>>>>>>>>>>> AREA DE VALIDAÇÃO DE EXISTES E INEXISTENTES <<<<<<<<<<<<
print('\n')
print("Lista 1 --> " + str(lstFiles1))
# COMPARAÇÃO EXISTENCIA DIRETORIO PATH2 NO DIRETORIO PATH1
for i in range(int(len(lstFiles1))):
	#  TRATAMENTO DE NAO EXISTENCIA DIRETORIO PATH2 NO DIRETORIO PATH1
	try:
		existInBothLsts.append(lstFiles2[lstFiles2.index(lstFiles1[i])])
	except ValueError as e:
		newInLstFiles1.append(lstFiles1[i])


print('\n')
print("Lista 2 --> " + str(lstFiles2))
# COMPARAÇÃO EXISTENCIA DIRETORIO PATH2 NO DIRETORIO PATH1
for i in range(int(len(lstFiles2))):
	#  TRATAMENTO DE NAO EXISTENCIA DIRETORIO PATH2 NO DIRETORIO PATH1
	try:
		lstFiles1[lstFiles1.index(lstFiles2[i])]
	except ValueError as e:
		newInLstFiles2.append(lstFiles2[i])

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||



print('\n')
print("New In List 1 ------------> " + str(newInLstFiles1))
print("New In List 2 ------------> " + str(newInLstFiles2))
print("In Both Lists ------------> " + str(existInBothLsts))


numberOfMissingLines = []

for currentFile in existInBothLsts:

	contadorDiffT1 = 0
	contadorDiffT2 = 0
	with open(path1 + currentFile, "r", encoding="utf8", errors="ignore") as fileT1, open(path2 + currentFile,"r", encoding="utf8", errors="ignore") as fileT2:


		# >>>>>>>>>>>> AREA DE COMPARAÇÃO DE LINHAS FALTANTES  <<<<<<<<<<<<
		
		# FATIAR DE LINHAS DE UM ARQUIVO
		fileArrayT1 = fileT1.read().split('\n')
		fileArrayT2 = fileT2.read().split('\n')		

		if len(fileArrayT1) >= len(fileArrayT2):
			missingLines = len(fileArrayT1) - len(fileArrayT2)
			# print(len(fileArrayT1) - len(fileArrayT2))
		else:
			missingLines = len(fileArrayT2) - len(fileArrayT1)
			# print(len(fileArrayT2) - len(fileArrayT1))
		#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

		
		# >>>>>>>>>>>> AREA DE COMPARAÇÃO DE LINHAS DIFERENTES <<<<<<<<<<<<
		
		for contadorT2 in range(len(fileArrayT2)):
			if fileArrayT2[contadorT2] in fileArrayT1:
				pass
			else:
				contadorDiffT2 += 1

		for contadorT1 in range(len(fileArrayT1)):
			if fileArrayT1[contadorT1] in fileArrayT2:
				pass
			else:
				contadorDiffT1 += 1

		#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
		if contadorDiffT1 >= contadorDiffT2:
			finalArrayOfExisting.append([currentFile, missingLines, contadorDiffT2, missingLines + contadorDiffT2])
		else:
			finalArrayOfExisting.append([currentFile, missingLines, contadorDiffT1, missingLines + contadorDiffT1])

print()			
print("Array Final --> " + str(finalArrayOfExisting))
print()			
print("------------------------------------")			
print("--- JOB  -  DIFERENCA TOTAL --------")			
print("------------------------------------")			
print()
for f  in finalArrayOfExisting:
	print(f[0] + " - " + str(f[3]))			

print()
print("************************************")			


