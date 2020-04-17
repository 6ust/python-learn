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
newInLstFiles1 = []
newInLstFiles2 = []
existInBothLsts    = []



# LISTAGEM DE ARQUIVOS DE UM DIRETORIO
for r, d, f in os.walk(path1):
	for file in f:
		if "" in file:
			lstFiles1.append(os.path.join(r, file)[len(path1):])

for r, d, f in os.walk(path2):
	for file in f:
		if "" in file:
			lstFiles2.append(os.path.join(r, file)[len(path1):])


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




print('\n')
print("New In List 1 ------------> " + str(newInLstFiles1))
print("New In List 2 ------------> " + str(newInLstFiles2))
print("In Both Lists ----------> " + str(existInBothLsts))