import os
import re

# CAMINHO DOS DIRETORIOS
pathDefault = "."
path1 = pathDefault + "\\t1\\"
path2 = pathDefault + "\\t2\\"

diffFileT1   = []
diffFileT2   = []

# >>>>>>>>>>>> AREA DE COMPARAÇÃO DE LINHAS DIFERENTES <<<<<<<<<<<<

# currentFile = 'JIM0010'
currentFile = 'JIM0020'

with open(path1 + currentFile, "r", encoding="utf8", errors="ignore") as fileT1, open(path2 + currentFile, "r", encoding="utf8", errors="ignore") as fileT2:

	# FATIAR DE LINHAS DE UM ARQUIVO
	fileArrayT1 = fileT1.read().split('\n')
	fileArrayT2 = fileT2.read().split('\n')

	print("\n\n" + currentFile)
	for f in fileArrayT1:
		print(f)

	for f in fileArrayT1:
		print(f)
		
	for contadorT1 in range(len(fileArrayT1)):
		if fileArrayT1[contadorT1] in fileArrayT2:
			print("Existe....")
		else:
			print("NOT Existe....")


#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
